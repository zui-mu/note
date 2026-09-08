# Pymata4EX、传感器与 RGB 灯

## 一、这节课在做什么

Python 程序通过 `pymata4EX` 与开发板通信。开发板负责把引脚上的电压状态转换为数据，或者把 Python 指令输出到引脚；Python 负责读取数据、判断条件和控制灯光。

本节练习可以归成一条完整流程：

```text
连接开发板
    -> 配置引脚模式
    -> 读取传感器数值
    -> 用 if 判断条件
    -> digital_write 或 pwm_write 控制 RGB 灯
    -> 延时后重复
```

课堂展示照片见：[classroom-presentation.jpg](../assets/classroom-presentation.jpg)。

## 二、第一步：导入模块并连接开发板

```python
import time
from MyClass import pymata4EX

board = pymata4EX.Pymata4EX()
```

- `time` 提供 `time.sleep()`，让程序暂停一小段时间。
- `pymata4EX` 是课程使用的开发板通信库。
- `Pymata4EX()` 创建一个名为 `board` 的对象，后面的读写操作都通过它完成。

连接失败时，先检查 USB 线、开发板端口、Firmata 程序和 `MyClass` 文件夹是否在 Python 可导入的位置。

## 三、第二步：认识引脚与模式

### 1. 本节接线

| 元件 | 引脚 | 类型 | 程序中的常量 |
| --- | ---: | --- | --- |
| 光敏传感器 | A0 / 0 | 模拟输入 | `LIGHT_PIN = 0` |
| 声音传感器 | A1 / 1 | 模拟输入 | `SOUND_PIN = 1` |
| 滑动变阻器 | A2 / 2 | 模拟输入 | `SLIDE_PIN = 2` |
| RGB 红色通道 | 5 | 数字输出 / PWM 输出 | `RED_PIN = 5` |
| RGB 绿色通道 | 6 | 数字输出 / PWM 输出 | `GREEN_PIN = 6` |
| RGB 蓝色通道 | 10 | 数字输出 / PWM 输出 | `BLUE_PIN = 10` |

把数字写成常量名的好处是：接线变动时只改一处，程序也更容易读。

### 2. 模拟输入与数字输出

```python
board.set_pin_mode_analog_input(LIGHT_PIN)
board.set_pin_mode_analog_input(SOUND_PIN)

board.set_pin_mode_digital_output(RED_PIN)
board.set_pin_mode_digital_output(GREEN_PIN)
board.set_pin_mode_digital_output(BLUE_PIN)
```

- `set_pin_mode_analog_input(pin)`：把引脚设为模拟输入，用于读取连续变化的传感器数值。
- `set_pin_mode_digital_output(pin)`：把引脚设为数字输出，只输出 `0` 或 `1`。
- `set_pin_mode_pwm_output(pin)`：把引脚设为 PWM 输出，用于控制亮度，取值通常为 `0` 到 `255`。

一个引脚在使用前必须先配置正确模式。模拟输入、数字输出和 PWM 输出是不同的工作方式。

## 四、第三步：读取模拟传感器

```python
light_value = board.analog_read(LIGHT_PIN)[0]
sound_value = board.analog_read(SOUND_PIN)[0]
slide_value = board.analog_read(SLIDE_PIN)[0]
```

`analog_read()` 返回的数据中，第一个元素 `[0]` 是当前读数。读数常见范围是 `0` 到 `1023`，但具体含义取决于模块接线和环境。

```python
print("光敏:", light_value, "声音:", sound_value)
```

先把读数打印出来，再决定阈值。课堂给出的观察值为：光敏传感器白天约 `78`，大于 `200` 可暂时当作夜晚；环境声音约 `400`，大于 `500` 暂时当作检测到声音。这些不是固定标准，实际使用时应重新测量。

## 五、第四步：数字方式控制 RGB 灯

```python
board.digital_write(RED_PIN, 1)
board.digital_write(GREEN_PIN, 0)
board.digital_write(BLUE_PIN, 0)
```

`digital_write(pin, value)` 只写入两种状态：

| 值 | 含义 |
| ---: | --- |
| `1` | 高电平，本套示例中对应点亮该颜色通道 |
| `0` | 低电平，本套示例中对应关闭该颜色通道 |

RGB 灯由红、绿、蓝三个通道混色：

| 红 | 绿 | 蓝 | 显示颜色 |
| ---: | ---: | ---: | --- |
| 1 | 0 | 0 | 红 |
| 0 | 1 | 0 | 绿 |
| 0 | 0 | 1 | 蓝 |
| 1 | 1 | 0 | 黄 |
| 1 | 0 | 1 | 紫 |
| 0 | 1 | 1 | 青 |
| 1 | 1 | 1 | 白 |

有些 RGB 模块是共阳极，电平逻辑可能相反：写入 `0` 才会点亮。若实际现象与表格相反，把通道值取反即可；先用单色测试确认硬件类型。

## 六、第五步：用 PWM 调节亮度

```python
board.set_pin_mode_pwm_output(RED_PIN)
board.pwm_write(RED_PIN, 128)
```

PWM 不是连续模拟电压，而是快速切换高低电平；通过改变高电平所占的时间比例来表现不同亮度。

| PWM 值 | 亮度效果 |
| ---: | --- |
| `0` | 熄灭 |
| `128` | 大约半亮 |
| `255` | 最亮 |

渐亮的核心是循环增加 PWM 值：

```python
for value in range(0, 256, 5):
    board.pwm_write(RED_PIN, value)
    time.sleep(0.025)
```

`range(0, 256, 5)` 从 `0` 开始，每次增加 `5`，最后不超过 `255`。渐暗时把步长改成负数：`range(255, -1, -5)`。

## 七、第六步：把两个传感器组合成楼道灯

课堂逻辑是：只有在夜晚并且有声音时才开灯。

```text
光敏值 > 200 ?
├── 否：白天，关灯
└── 是：夜晚
    ├── 声音值 > 500：开灯
    └── 声音值 <= 500：关灯
```

对应的嵌套条件：

```python
if light_value > LIGHT_THRESHOLD:
    if sound_value > SOUND_THRESHOLD:
        light_on()
    else:
        light_off()
else:
    light_off()
```

这里的 `light_on()` 和 `light_off()` 是函数。把重复的三次 RGB 写入操作收进函数，能让主逻辑专注表达“什么条件下开灯”。

## 八、循环、延时与安全结束

```python
while True:
    # 重复执行的任务
    time.sleep(1)
```

- `while True` 表示无限循环，适合持续读取传感器的设备。
- `time.sleep(1)` 每轮暂停 1 秒，避免终端输出过快，也避免不必要地频繁读取。
- 用 `Ctrl+C` 可以结束程序。
- 示例将关闭灯和 `board.shutdown()` 放在 `finally` 中，使程序被中断时仍会尽量收尾。

## 九、常见排查顺序

1. 开发板连不上：确认 USB 线、端口、Firmata 和 `MyClass` 的位置。
2. 没有传感器数值：检查是否用了 `set_pin_mode_analog_input()`，以及模块是否接到对应 A0/A1/A2。
3. RGB 灯不亮或颜色相反：核对三个通道的实际接线，确认共阳极/共阴极逻辑。
4. 渐变不明显：确认引脚已设置为 PWM 输出，并检查模块是否支持该引脚的 PWM。
5. 楼道灯误触发：先打印真实环境中的读数，再微调两个阈值。

## 十、课堂小结

这节课的重点不是背 API，而是建立“输入 - 判断 - 输出”的程序结构：传感器提供输入数据，`if` 决定行为，RGB 灯把结果显示出来。数字输出适合开关和基础混色，PWM 输出适合亮度与渐变；将这两种输出方式结合传感器判断，就能做出楼道感应灯这样的基础交互装置。
