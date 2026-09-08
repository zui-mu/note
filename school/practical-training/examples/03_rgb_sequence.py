import time

from MyClass import pymata4EX


RED_PIN = 5
GREEN_PIN = 6
BLUE_PIN = 10

board = pymata4EX.Pymata4EX()

board.set_pin_mode_digital_output(RED_PIN)
board.set_pin_mode_digital_output(GREEN_PIN)
board.set_pin_mode_digital_output(BLUE_PIN)


def turn_off_all():
    board.digital_write(RED_PIN, 0)
    board.digital_write(GREEN_PIN, 0)
    board.digital_write(BLUE_PIN, 0)


def blink(pin, times=3, interval=0.5):
    for _ in range(times):
        board.digital_write(pin, 1)
        time.sleep(interval)
        board.digital_write(pin, 0)
        time.sleep(interval)


try:
    while True:
        turn_off_all()
        board.digital_write(RED_PIN, 1)
        time.sleep(3)
        board.digital_write(RED_PIN, 0)
        blink(RED_PIN)

        board.digital_write(BLUE_PIN, 1)
        time.sleep(1)
        board.digital_write(BLUE_PIN, 0)
        blink(BLUE_PIN)

        board.digital_write(GREEN_PIN, 1)
        time.sleep(3)
        board.digital_write(GREEN_PIN, 0)
        blink(GREEN_PIN)
except KeyboardInterrupt:
    print("\n程序已停止。")
finally:
    turn_off_all()
    board.shutdown()
