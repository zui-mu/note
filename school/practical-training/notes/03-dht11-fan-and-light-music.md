# DHT11、温控风扇与灯光旋律

## 一、今天的课堂主线

今天从“读取一个传感器”进一步走到了“根据传感器控制设备”，还把蜂鸣器、RGB 灯和列表组合成了一个小型声光作品：

```text
DHT11 温湿度传感器
    -> 读取温度和湿度
    -> 比较温度阈值
    -> 数字输出控制风扇

音符列表
    -> for 循环逐个取出频率和时值
    -> 蜂鸣器发声 + RGB 灯同步亮起
```

对应代码：

- [10_dht11_read.py](../examples/10_dht11_read.py)
- [11_temperature_fan_control.py](../examples/11_temperature_fan_control.py)
- [12_buzzer_rgb_music.py](../examples/12_buzzer_rgb_music.py)

## 二、DHT11 温湿度传感器

### 1. 配置 DHT 引脚

```python
DHT_PIN = 2
board.set_pin_mode_dht(DHT_PIN, sensor_type=11)
```

`DHT_PIN = 2` 表示 DHT11 的数据线接在 2 号引脚。`sensor_type=11` 表示使用 DHT11 型号；如果换成 DHT22，传感器类型参数通常也需要相应修改。

### 2. 读取返回值

```python
value = board.dht_read(DHT_PIN)
humidity = value[0]
temperature = value[1]
```

本课程库返回的数据可以按下标读取：

| 表达式 | 含义 |
| --- | --- |
| `value[0]` | 湿度，单位为 `%` |
| `value[1]` | 温度，单位为 `℃` |

这里的 `value` 是一次读取结果，`value[0]` 和 `value[1]` 是结果中的两个位置。读取后先分别保存为 `humidity` 和 `temperature`，程序会更容易理解。

### 3. 传感器读取可能暂时失败

```python
if value is not None:
    print(f"湿度: {value[0]} %, 温度: {value[1]} ℃")
else:
    print("暂时没有读取到 DHT11 数据")
```

传感器通信可能因为接线、供电或读取时机暂时没有返回有效数据，所以程序不能无条件地马上访问 `value[0]`。先判断是否为 `None`，是一个更稳妥的写法。

## 三、温度控制风扇

### 1. 风扇是数字输出

```python
FAN_PIN = 3
board.set_pin_mode_digital_output(FAN_PIN)
```

课堂示例把风扇当作开关设备：写入 `1` 开启，写入 `0` 关闭。实际接线中风扇通常需要三极管、继电器或驱动模块，不能直接让开发板引脚承担电机电流；这里的程序只负责输出控制信号。

### 2. 普通阈值判断

最直接的逻辑是：

```python
if temperature >= 29:
    board.digital_write(FAN_PIN, 1)
elif temperature <= 28:
    board.digital_write(FAN_PIN, 0)
```

注意 `if` 和 `elif` 的条件互相覆盖了两个区间，中间的 `28 < temperature < 29` 没有动作。

### 3. 回差（滞回）为什么有用

课堂注释里的“回差”是控制系统中很实用的思想：

```text
温度 >= 29℃  -> 开风扇
温度 <= 28℃  -> 关风扇
28℃ < 温度 < 29℃ -> 保持上一次状态
```

如果只使用一个阈值，例如温度大于 28℃ 开、低于 28℃ 关，传感器在阈值附近轻微波动时，风扇会反复启停。设置两个阈值后，风扇一旦开启，要等温度降到更低的 `28℃` 才关闭；这样可以减少抖动。

代码中用 `fan_is_on` 记录状态：

```python
if temperature >= TEMP_HIGH and not fan_is_on:
    board.digital_write(FAN_PIN, 1)
    fan_is_on = True
elif temperature <= TEMP_LOW and fan_is_on:
    board.digital_write(FAN_PIN, 0)
    fan_is_on = False
```

这说明控制程序不仅要看当前传感器值，有时还要保存“上一次设备状态”。

## 四、蜂鸣器和 RGB 灯同步

### 1. 同时配置两种输出

```python
board.set_pin_mode_tone(TONE_PIN)
board.set_pin_mode_digital_output(RED_PIN)
board.set_pin_mode_digital_output(GREEN_PIN)
board.set_pin_mode_digital_output(BLUE_PIN)
```

蜂鸣器使用 tone 模式，RGB 三个通道使用数字输出。它们互不冲突，可以在同一个函数中同时控制。

### 2. 用二元组保存“音符 + 时值”

```python
SONG = [
    (C, 1), (C, 1), (G, 1), (G, 1),
    (A, 1), (A, 1), (G, 2),
]
```

这里的每个元素是一个二元组：

- 第一个位置是频率，例如 `C = 262`。
- 第二个位置是时值，例如 `2` 表示比 `1` 持续两倍的节拍。

```python
for frequency, length in SONG:
    play_note(frequency, length)
```

这叫作序列解包：每轮循环自动把二元组的两个位置分别放进 `frequency` 和 `length`。相比使用 `song[i][0]`、`song[i][1]`，可读性更好。

### 3. 一个音符由四个动作组成

```python
def play_note(frequency, length):
    light_on()
    board.play_tone_continuously(TONE_PIN, frequency)
    time.sleep(BEAT * length * 0.85)

    board.play_tone_off(TONE_PIN)
    light_off()
    time.sleep(BEAT * length * 0.15)
```

一个音符的流程是：

1. 打开白色 RGB 灯。
2. 让蜂鸣器播放指定频率。
3. 等待总时长的 `85%`，作为发声部分。
4. 关闭蜂鸣器和灯，再等待剩余 `15%`，形成音符间隔。

`0.85 + 0.15 = 1`，所以一个音符的总时长仍然是 `BEAT * length`。停顿会让旋律更清楚，也能让相邻音符分开。

## 五、今天新增的 Python 知识点

| 知识点 | 在课堂代码中的体现 |
| --- | --- |
| 传感器类型配置 | `set_pin_mode_dht(..., sensor_type=11)` |
| 返回值下标 | `value[0]` 湿度、`value[1]` 温度 |
| 空值判断 | `value is not None` |
| 状态变量 | `fan_is_on` 记录风扇当前状态 |
| 回差控制 | `TEMP_HIGH` 与 `TEMP_LOW` 分开设置 |
| 二元组列表 | `(frequency, length)` 保存音符和时值 |
| 序列解包 | `for frequency, length in SONG` |
| 函数参数 | `play_note(frequency, length)` |
| 多设备协同 | 一个音符函数同时控制蜂鸣器和 RGB 灯 |
| 资源释放 | `finally` 中关闭风扇、蜂鸣器、灯并调用 `shutdown()` |

## 六、今天的课堂总结

前面的程序主要是“读数并显示”或“按条件点灯”，今天开始出现了更完整的自动控制系统：DHT11 提供环境数据，程序根据带回差的规则决定风扇状态；列表负责保存旋律数据，函数负责执行播放动作，蜂鸣器和 RGB 灯共同产生输出。可以把这类程序概括为：

```text
配置硬件 -> 采集数据 -> 保存状态或数据 -> 判断/遍历 -> 控制多个输出 -> 清理资源
```
