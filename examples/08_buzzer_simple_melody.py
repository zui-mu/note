import time

from MyClass import pymata4EX


TONE_PIN = 4

board = pymata4EX.Pymata4EX()
board.set_pin_mode_tone(TONE_PIN)

MELODY = [262, 262, 392, 392, 440, 440, 392]
DURATIONS = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.0]

try:
    for frequency, duration in zip(MELODY, DURATIONS):
        board.play_tone_continuously(TONE_PIN, frequency)
        time.sleep(duration)
finally:
    board.play_tone_off(TONE_PIN)
    board.shutdown()
