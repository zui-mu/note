# 滑动变阻器与蜂鸣器

## 一、今天新增的程序结构

今天的两个例子把“输入”和“输出”连接得更直接：

```text
滑动变阻器模拟值
    -> 数值范围转换
    -> PWM 亮度

音符频率 + 节拍时长
    -> 蜂鸣器音调
    -> 列表和循环播放旋律
```

配套代码：

- [07_potentiometer_led_brightness.py](../examples/07_potentiometer_led_brightness.py)
- [08_buzzer_simple_melody.py](../examples/08_buzzer_simple_melody.py)
- [09_buzzer_melody_lists.py](../examples/09_buzzer_melody_lists.py)

## 二、滑动变阻器控制 LED 亮度

### 1. 配置模拟输入和 PWM 输出

```python
analog_pin = 2
r_led = 5

board.set_pin_mode_analog_input(analog_pin)
board.set_pin_mode_pwm_output(r_led)
```

滑动变阻器接在 A2，所以用 `analog_input` 读取；红色 LED 接在 5 号 PWM 引脚，所以用 `pwm_output` 控制亮度。输入和输出的引脚模式必须分别设置。

### 2. 读取数值并转换范围

```python
value = board.analog_read(analog_pin)[0]
brightness = int(value / 4)
```

模拟读数通常在 `0~1023`，PWM 亮度通常在 `0~255`。因为 `1023 / 4` 约等于 `255`，所以课堂示例用除以 `4` 完成近似转换：

```text
滑动值 0       -> 亮度 0
滑动值 1023    -> 亮度约 255
```

更精确的线性写法是：

```python
brightness = int(value * 255 / 1023)
```

这体现了一个常见思想：把一个范围的数值映射到另一个范围。`int()` 会去掉小数部分，得到开发板需要的整数 PWM 值。

### 3. 反复读取与缩进

正确的循环应该把读取、转换、输出和打印全部缩进到 `while True` 中：

```python
while True:
    time.sleep(0.05)
    value = board.analog_read(analog_pin)[0]
    brightness = int(value * 255 / 1023)
    board.pwm_write(r_led, brightness)
```

`while True: time.sleep(0.05)` 这种写法虽然是合法的单行循环，但它会永远只执行睡眠，后面的读取代码不会执行。因此，循环体的缩进是本例最需要注意的地方。

`0.05` 秒等于 50 毫秒，刷新足够快，旋钮变化时灯光会比较平滑；同时又不会让程序毫无间隔地占用通信。

## 三、蜂鸣器的基础控制

### 1. 设置 tone 模式

```python
tone_pin = 4
board.set_pin_mode_tone(tone_pin)
```

蜂鸣器接在 4 号引脚。`set_pin_mode_tone()` 把引脚设置为音调输出模式。

### 2. 频率决定音高

```python
board.play_tone_continuously(tone_pin, 262)
time.sleep(0.5)
```

第二个参数是频率，单位是赫兹（Hz）。频率越高，听起来音调越高；`time.sleep()` 决定这个音符持续多久。

课堂示例中的几个频率大致对应：

| 频率 | 简谱音名 | 说明 |
| ---: | --- | --- |
| 262 | 低音 1（C） | `do` |
| 392 | 低音 5（G） | `sol` |
| 440 | 中音 6（A） | `la` |

`play_tone_continuously()` 会让当前音调保持到下一次改变音调或关闭声音。播放完毕要调用：

```python
board.play_tone_off(tone_pin)
```

### 3. 简短旋律的结构

```python
board.play_tone_continuously(tone_pin, 262)
time.sleep(0.5)
board.play_tone_continuously(tone_pin, 262)
time.sleep(0.5)
board.play_tone_continuously(tone_pin, 392)
time.sleep(0.5)
```

每个“播放频率 + 等待时间”组成一个音符。按顺序写出几个音符可以快速验证蜂鸣器和接线是否正常，但音符较多时会产生重复代码，所以课堂文件进一步使用列表和循环。

## 四、用列表保存旋律

### 1. 音符表

```python
CL = [0, 262, 294, 330, 349, 392, 440, 494]
CM = [0, 523, 587, 659, 698, 784, 880, 988]
CH = [0, 1046, 1175, 1318, 1397, 1568, 1760, 1976]
```

列表是一组有顺序的数据。`CL[1]` 表示低音 1，`CM[1]` 表示中音 1，`CH[1]` 表示高音 1。Python 列表从下标 `0` 开始，因此 `CL[0]` 被设计成 `0`，可以作为停顿或空音符。

使用 `CL[5]` 比直接写 `392` 更容易理解，也方便以后统一调整音高。

### 2. 音符列表和节拍列表

```python
song = [CM[1], CM[1], CM[5], CM[5], CM[6], CM[6], CM[5]]
beat = [2, 2, 2, 2, 2, 2, 4]

for i in range(len(song)):
    board.play_tone_continuously(tone_pin, song[i])
    time.sleep(beat[i] * 0.25)
```

两个列表通过相同的下标对应起来：`song[i]` 是第 `i` 个音符，`beat[i]` 是它的节拍长度。`len(song)` 返回音符列表的长度，`range()` 负责依次产生下标。

这叫作并行列表。它要求两个列表长度一致，否则可能出现下标越界或音符和节拍错位。

### 3. 用函数封装歌曲

```python
def play_song(song, beat):
    for i in range(len(song)):
        board.play_tone_continuously(tone_pin, song[i])
        time.sleep(beat[i] * 0.25)
        board.play_tone_continuously(tone_pin, CL[0])
        time.sleep(0.08)
```

函数把“播放一首歌”的重复逻辑封装起来。以后只需要传入不同的 `song` 和 `beat` 列表，就可以复用同一套播放代码。

课堂文件还用 `play_happy_birthday()` 和 `play_star()` 分别保存两首旋律，最后在 `main()` 中循环调用。这体现了“数据放进列表，动作放进函数”的组织方式。

## 五、两个例子的对比

| 对比项 | 滑动变阻器 + LED | 蜂鸣器旋律 |
| --- | --- | --- |
| 输入或数据 | A2 的模拟读数 | 频率、音符和节拍列表 |
| 输出方式 | `pwm_write()` | `play_tone_continuously()` |
| 控制变量 | `brightness` | 音符频率与持续时间 |
| 主要结构 | `while True` 持续响应 | `for` 按顺序播放 |
| 核心知识 | 范围映射、缩进、实时刷新 | 列表、下标、`len()`、函数 |

## 六、今天的知识点总结

1. 同一个开发板可以同时使用不同类型的引脚模式：模拟输入、PWM 输出和 tone 输出。
2. 传感器读数不一定能直接作为输出参数，需要先做范围映射。
3. `while True` 适合持续响应实时输入；`for` 适合按顺序遍历有限的数据。
4. 列表可以把一组有顺序的音符或节拍保存起来，下标用来访问其中一个元素。
5. `len()` 可以获得列表长度，和 `range()` 配合可以遍历整个列表。
6. `0` 不只是数字，也可以在音符表中表示停顿。
7. 函数可以把重复动作封装起来，让主程序更清楚。
8. 硬件程序要在结束时关闭蜂鸣器，并尽量调用 `board.shutdown()` 释放连接。
