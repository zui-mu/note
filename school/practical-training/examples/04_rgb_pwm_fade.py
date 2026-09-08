import time

from MyClass import pymata4EX


RED_PIN = 5
GREEN_PIN = 6
BLUE_PIN = 10

board = pymata4EX.Pymata4EX()

board.set_pin_mode_pwm_output(RED_PIN)
board.set_pin_mode_pwm_output(GREEN_PIN)
board.set_pin_mode_pwm_output(BLUE_PIN)

# Seven base colors at full brightness.
COLORS = [
    (255, 0, 0),
    (255, 160, 0),
    (255, 255, 0),
    (0, 255, 0),
    (0, 255, 255),
    (0, 0, 255),
    (160, 0, 255),
]


def set_color(red, green, blue):
    board.pwm_write(RED_PIN, red)
    board.pwm_write(GREEN_PIN, green)
    board.pwm_write(BLUE_PIN, blue)


def fade_to(red_max, green_max, blue_max, brightness):
    set_color(
        int(red_max * brightness / 255),
        int(green_max * brightness / 255),
        int(blue_max * brightness / 255),
    )


try:
    while True:
        for red_max, green_max, blue_max in COLORS:
            for brightness in range(0, 256, 5):
                fade_to(red_max, green_max, blue_max, brightness)
                time.sleep(0.025)

            for brightness in range(255, -1, -5):
                fade_to(red_max, green_max, blue_max, brightness)
                time.sleep(0.025)
except KeyboardInterrupt:
    print("\n程序已停止。")
finally:
    set_color(0, 0, 0)
    board.shutdown()
