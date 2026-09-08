import time

from MyClass import pymata4EX


LIGHT_PIN = 0  # A0: light sensor
SOUND_PIN = 1  # A1: sound sensor
SLIDE_PIN = 2  # A2: slide potentiometer

board = pymata4EX.Pymata4EX()

board.set_pin_mode_analog_input(LIGHT_PIN)
board.set_pin_mode_analog_input(SOUND_PIN)
board.set_pin_mode_analog_input(SLIDE_PIN)

try:
    while True:
        light_value = board.analog_read(LIGHT_PIN)[0]
        sound_value = board.analog_read(SOUND_PIN)[0]
        slide_value = board.analog_read(SLIDE_PIN)[0]

        print(
            "光敏:", light_value,
            "声音:", sound_value,
            "滑动变阻器:", slide_value,
        )
        time.sleep(1)
except KeyboardInterrupt:
    print("\n程序已停止。")
finally:
    board.shutdown()
