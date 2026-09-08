import time

from MyClass import pymata4EX


RED_PIN = 5
GREEN_PIN = 6
BLUE_PIN = 10

board = pymata4EX.Pymata4EX()

board.set_pin_mode_pwm_output(RED_PIN)
board.set_pin_mode_pwm_output(GREEN_PIN)
board.set_pin_mode_pwm_output(BLUE_PIN)


def set_pwm(red, green, blue):
    board.pwm_write(RED_PIN, red)
    board.pwm_write(GREEN_PIN, green)
    board.pwm_write(BLUE_PIN, blue)


try:
    # Fixed-color example shown after the fade demonstration.
    set_pwm(130, 50, 70)
    time.sleep(3)

    # Red fades up and down, matching the classroom PWM loop idea.
    while True:
        for value in range(0, 256, 5):
            set_pwm(value, 0, 0)
            time.sleep(0.1)

        for value in range(255, -1, -5):
            set_pwm(value, 0, 0)
            time.sleep(0.1)
except KeyboardInterrupt:
    print("\n程序已停止。")
finally:
    set_pwm(0, 0, 0)
    board.shutdown()
