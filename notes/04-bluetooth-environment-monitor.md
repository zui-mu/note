# 蓝牙环境信息监测系统

## 一、课堂作业目标

这次作业把前面学过的传感器读数进一步扩展成了一个电脑端监测系统。开发板通过蓝牙串口把温度、湿度、距离、光照等数据发送到电脑，电脑上的 Python 程序负责连接串口、解析数据、更新界面和绘制实时曲线。

对应代码：

- [13_bluetooth_environment_monitor.py](../examples/13_bluetooth_environment_monitor.py)

整体流程可以理解为：

```text
开发板采集传感器
    -> 蓝牙串口发送字符串
    -> Python 串口线程接收
    -> 解析 T/H/D/L 四类数据
    -> PyQt5 界面显示数值
    -> pyqtgraph 绘制实时曲线
```

## 二、这段程序和前面代码的区别

前面的课堂代码主要运行在“开发板控制程序”这一侧，例如读取 DHT11、控制风扇、控制蜂鸣器和 RGB 灯。这次作业重点转到了“电脑上位机”这一侧。

| 前面代码 | 本次作业 |
| --- | --- |
| 直接用 `pymata4EX` 读写开发板引脚 | 用 `serial` 连接蓝牙串口 |
| 主要在终端里 `print` 输出 | 使用 PyQt5 创建图形界面 |
| 一边读传感器一边控制输出 | 接收开发板已经发送出来的数据 |
| 单个循环完成所有事情 | 用子线程接收串口，主线程更新界面 |

也就是说，这次程序更像一个“环境监测上位机”：硬件负责采集，电脑负责展示。

## 三、蓝牙串口通信

### 1. 导入串口库

```python
import serial
import serial.tools.list_ports
```

`serial` 来自 `pyserial` 库，用来打开串口并读取数据。`serial.tools.list_ports` 用来扫描电脑当前有哪些可用串口，方便在界面里选择蓝牙模块对应的端口。

如果电脑还没有安装这些库，可以先安装：

```powershell
pip install pyserial PyQt5 pyqtgraph
```

### 2. 打开串口

```python
self.ser = serial.Serial(
    port=self.port,
    baudrate=9600,
    timeout=1
)
```

这行代码会连接指定串口。

| 参数 | 含义 |
| --- | --- |
| `port` | 串口号，例如 `COM3`、`COM5` |
| `baudrate=9600` | 波特率，必须和开发板发送端一致 |
| `timeout=1` | 最多等待 1 秒，避免程序一直卡住 |

蓝牙模块在电脑上通常会表现为一个普通串口，所以程序不需要直接处理蓝牙协议，只要按串口方式读取即可。

### 3. 读取一行数据

```python
line = self.ser.readline().decode("utf-8", errors="ignore").strip()
```

`readline()` 会读取一行字节数据，`decode()` 把字节转换成字符串，`strip()` 去掉两端多余的换行和空格。

开发板发送的数据格式假设类似：

```text
T:26.5;H:62.0;D:13.2;L:583;
```

其中：

| 标记 | 含义 |
| --- | --- |
| `T` | temperature，温度 |
| `H` | humidity，湿度 |
| `D` | distance，距离 |
| `L` | light，光照 ADC 值 |

## 四、解析字符串数据

课堂代码用字典保存解析结果：

```python
values = {}

for item in line.strip(";").split(";"):
    if ":" in item:
        key, value = item.split(":", 1)
        values[key] = value
```

这段代码的意思是：

1. 先去掉末尾多余的分号。
2. 用 `;` 把一整行分成多个小段。
3. 每个小段再用 `:` 分成键和值。
4. 存入字典，例如 `values["T"] = "26.5"`。

当四项数据都存在时，再转换类型：

```python
temperature = float(values["T"])
humidity = float(values["H"])
distance = float(values["D"])
light = int(values["L"])
```

温度、湿度、距离可能带小数，所以用 `float`；光照是 ADC 数值，通常是整数，所以用 `int`。

## 五、为什么要用线程

PyQt5 的窗口界面运行在主线程。如果直接在主线程里不断读取串口，界面可能会卡住，按钮也可能点不动。

所以程序定义了一个串口线程：

```python
class SerialThread(QThread):
    data_received = pyqtSignal(float, float, float, int)
```

`QThread` 负责在后台持续接收数据。`pyqtSignal` 是信号，用来把后台线程收到的数据安全地传给界面。

信号发出：

```python
self.data_received.emit(
    temperature,
    humidity,
    distance,
    light
)
```

信号连接到界面更新函数：

```python
self.serial_thread.data_received.connect(self.update_data)
```

这就是 PyQt 中常见的“子线程干活，主线程更新界面”的写法。

## 六、界面结构

程序用 `QMainWindow` 创建主窗口，用 `QWidget` 和布局管理器安排控件。

```python
main_layout = QVBoxLayout(central_widget)
connection_layout = QHBoxLayout()
sensors_layout = QGridLayout()
```

| 布局 | 用途 |
| --- | --- |
| `QVBoxLayout` | 从上到下排列标题、连接栏、传感器面板 |
| `QHBoxLayout` | 横向排列串口选择框、刷新按钮、连接按钮 |
| `QGridLayout` | 网格排列温度、湿度、距离、光照四张卡片 |

每一个传感器卡片都由 `SensorPanel` 类创建，里面包含标题、当前数值、单位和一张曲线图。这样温度、湿度、距离、光照可以复用同一套界面结构。

## 七、实时曲线和数据缓存

程序用 `deque(maxlen=60)` 保存最近 60 个数据点：

```python
self.time_data = deque(maxlen=60)
self.temperature_data = deque(maxlen=60)
self.humidity_data = deque(maxlen=60)
self.distance_data = deque(maxlen=60)
self.light_data = deque(maxlen=60)
```

`deque` 的特点是：当数据超过 `maxlen` 后，最旧的数据会自动被挤掉。这样程序长时间运行时，曲线不会无限变长，也不会越来越占内存。

更新曲线时，把数据交给 pyqtgraph：

```python
self.curve.setData(list(times), list(values))
```

每次收到新数据后，程序会：

```text
更新数字显示
    -> 记录当前时间
    -> 追加传感器数据
    -> 重新绘制四条曲线
```

## 八、连接、断开和异常处理

### 1. 刷新串口

```python
ports = serial.tools.list_ports.comports()
```

这会扫描电脑上的串口列表，并把每个串口加入下拉框。

### 2. 连接按钮

连接按钮的逻辑是：如果当前没有线程，就创建线程并开始连接；如果已经连接，就断开。

```python
if self.serial_thread is not None:
    self.disconnect_serial()
    return
```

### 3. 程序关闭时释放资源

```python
def closeEvent(self, event):
    if self.serial_thread is not None:
        self.serial_thread.stop()
    event.accept()
```

串口和线程都属于外部资源。关闭窗口时主动停止线程、关闭串口，可以避免端口被占用，下一次运行程序时也更稳定。

## 九、今天新增的 Python 知识点

| 知识点 | 作用 |
| --- | --- |
| `serial.Serial` | 打开蓝牙串口并读取数据 |
| `list_ports.comports()` | 扫描电脑上的可用串口 |
| `decode()` | 把串口收到的字节转换成字符串 |
| `split()` | 按分隔符拆分传感器数据 |
| 字典 `dict` | 用 `T/H/D/L` 保存解析后的数据 |
| `QThread` | 后台接收串口数据，避免界面卡住 |
| `pyqtSignal` | 在线程和界面之间传递数据 |
| `QMainWindow` | 创建主窗口 |
| `QVBoxLayout/QHBoxLayout/QGridLayout` | 管理界面控件排列 |
| `QComboBox` | 选择蓝牙串口 |
| `QMessageBox` | 弹出提示或错误信息 |
| `pyqtgraph.PlotWidget` | 绘制实时曲线 |
| `deque(maxlen=60)` | 保存固定长度的历史数据 |
| `closeEvent` | 窗口关闭时释放资源 |

## 十、课堂总结

这次作业把“传感器项目”从开发板端扩展到了电脑端。它的核心不是单独某一个传感器，而是完整的数据链路：

```text
传感器采集 -> 蓝牙传输 -> 串口接收 -> 字符串解析 -> GUI 显示 -> 实时曲线
```

相比前面只在终端里打印数据，这个程序更接近真实项目里的上位机监控软件。它也说明了一个重要思路：硬件项目不一定只写控制引脚的代码，还可以写电脑端工具，把硬件采集到的数据变成更直观、更容易观察的界面。
