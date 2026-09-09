# Practical Training Notes

本仓库存放嵌入式实训课的 Markdown 笔记与 Python 示例。内容覆盖 2026-09-08 的 RGB 灯练习，以及 2026-09-09 的滑动变阻器、蜂鸣器和列表编程练习。

## 本次课程

- [知识点梳理：Pymata4EX、模拟输入与 RGB 灯](notes/01-pymata4ex-rgb-and-sensors.md)
- [新增知识点：滑动变阻器、PWM 亮度与蜂鸣器旋律](notes/02-potentiometer-and-buzzer.md)
- [课堂展示照片](assets/classroom-presentation.jpg)

## 可运行示例

运行前请确认开发板已连接、Firmata/Pymata 环境已就绪，并按实际接线核对引脚。

| 文件 | 内容 |
| --- | --- |
| [01_read_analog_sensors.py](examples/01_read_analog_sensors.py) | 读取光敏、声音和滑动变阻器三个模拟传感器 |
| [02_rgb_digital_colors.py](examples/02_rgb_digital_colors.py) | 用数字输出切换 RGB 灯的七种基础颜色 |
| [03_rgb_sequence.py](examples/03_rgb_sequence.py) | 红、蓝、绿灯的时序与闪烁练习 |
| [04_rgb_pwm_fade.py](examples/04_rgb_pwm_fade.py) | 用 PWM 实现七种颜色的渐亮渐暗 |
| [05_corridor_light.py](examples/05_corridor_light.py) | 光敏和声音传感器控制楼道灯 |
| [06_classroom_pwm_showcase.py](examples/06_classroom_pwm_showcase.py) | 根据课堂投影整理的 PWM 演示代码 |
| [07_potentiometer_led_brightness.py](examples/07_potentiometer_led_brightness.py) | 滑动变阻器实时控制红色 LED 亮度 |
| [08_buzzer_simple_melody.py](examples/08_buzzer_simple_melody.py) | 用频率和延时播放简短旋律 |
| [09_buzzer_melody_lists.py](examples/09_buzzer_melody_lists.py) | 课堂文件：用音符列表和节拍列表播放旋律 |

## 快速使用

在安装了课程提供的 `MyClass` 目录和 `pymata4EX` 后，在本目录执行：

```powershell
python examples/01_read_analog_sensors.py
```

用 `Ctrl+C` 结束程序。示例中的 `finally` 会关闭 RGB 灯并断开开发板连接。

## 目录说明

```text
practical training/
├── assets/     课堂图片等原始资料
├── examples/   可独立运行的 Python 程序
├── notes/      知识点和课堂总结
└── README.md   本次课程入口
```
