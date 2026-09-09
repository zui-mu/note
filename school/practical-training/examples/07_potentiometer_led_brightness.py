import time

from MyClass import pymata4EX


ANALOG_PIN = 2  # A2: slide potentiometer
RED_LED_PIN = 5

board = pymata4EX.Pymata4EX()

board.set_pin_mode_analog_input(ANALOG_PIN)
board.set_pin_mode_pwm_output(RED_LED_PIN)

try:
    while True:
        time.sleep(0.05)

        value = board.analog_read(ANALOG_PIN)[0]

        # Map the usual 0..1023 analog range to the 0..255 PWM range.
        brightness = int(value * 255 / 1023)
        board.pwm_write(RED_LED_PIN, brightness)

        print("滑动值:", value, "灯光亮度:", brightness)
except KeyboardInterrupt:
    print("\n程序已停止。")
finally:
    board.pwm_write(RED_LED_PIN, 0)
    board.shutdown()
