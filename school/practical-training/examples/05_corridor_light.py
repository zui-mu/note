import time

from MyClass import pymata4EX


LIGHT_PIN = 0  # A0: light sensor
SOUND_PIN = 1  # A1: sound sensor

RED_PIN = 5
GREEN_PIN = 6
BLUE_PIN = 10

# Measure your own environment and adjust these values if needed.
LIGHT_THRESHOLD = 200
SOUND_THRESHOLD = 500

board = pymata4EX.Pymata4EX()

board.set_pin_mode_analog_input(LIGHT_PIN)
board.set_pin_mode_analog_input(SOUND_PIN)

board.set_pin_mode_digital_output(RED_PIN)
board.set_pin_mode_digital_output(GREEN_PIN)
board.set_pin_mode_digital_output(BLUE_PIN)


def light_on():
    board.digital_write(RED_PIN, 1)
    board.digital_write(GREEN_PIN, 1)
    board.digital_write(BLUE_PIN, 1)


def light_off():
    board.digital_write(RED_PIN, 0)
    board.digital_write(GREEN_PIN, 0)
    board.digital_write(BLUE_PIN, 0)


try:
    while True:
        light_value = board.analog_read(LIGHT_PIN)[0]
        sound_value = board.analog_read(SOUND_PIN)[0]

        print("光敏 =", light_value, "| 声音 =", sound_value)

        if light_value > LIGHT_THRESHOLD:
            if sound_value > SOUND_THRESHOLD:
                light_on()
                print("晚上 + 有声音 -> 灯亮")
            else:
                light_off()
                print("晚上 + 没声音 -> 灯灭")
        else:
            light_off()
            print("白天 -> 灯灭")

        time.sleep(1)
except KeyboardInterrupt:
    print("\n程序已停止。")
finally:
    light_off()
    board.shutdown()
