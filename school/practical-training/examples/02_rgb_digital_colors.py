import time

from MyClass import pymata4EX


RED_PIN = 5
GREEN_PIN = 6
BLUE_PIN = 10

board = pymata4EX.Pymata4EX()

board.set_pin_mode_digital_output(RED_PIN)
board.set_pin_mode_digital_output(GREEN_PIN)
board.set_pin_mode_digital_output(BLUE_PIN)


def set_color(red, green, blue):
    board.digital_write(RED_PIN, red)
    board.digital_write(GREEN_PIN, green)
    board.digital_write(BLUE_PIN, blue)


COLORS = [
    ("红", 1, 0, 0),
    ("绿", 0, 1, 0),
    ("蓝", 0, 0, 1),
    ("黄", 1, 1, 0),
    ("紫", 1, 0, 1),
    ("青", 0, 1, 1),
    ("白", 1, 1, 1),
]

try:
    while True:
        for name, red, green, blue in COLORS:
            set_color(red, green, blue)
            print(f"当前颜色: {name}")
            time.sleep(1)
except KeyboardInterrupt:
    print("\n程序已停止。")
finally:
    set_color(0, 0, 0)
    board.shutdown()
