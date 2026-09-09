import time

from MyClass import pymata4EX


TONE_PIN = 4
RED_PIN = 5
GREEN_PIN = 6
BLUE_PIN = 10

board = pymata4EX.Pymata4EX()
board.set_pin_mode_tone(TONE_PIN)
board.set_pin_mode_digital_output(RED_PIN)
board.set_pin_mode_digital_output(GREEN_PIN)
board.set_pin_mode_digital_output(BLUE_PIN)

C = 262
D = 294
E = 330
F = 349
G = 392
A = 440

SONG = [
    (C, 1), (C, 1), (G, 1), (G, 1), (A, 1), (A, 1), (G, 2),
    (F, 1), (F, 1), (E, 1), (E, 1), (D, 1), (D, 1), (C, 2),
    (G, 1), (G, 1), (F, 1), (F, 1), (E, 1), (E, 1), (D, 2),
    (G, 1), (G, 1), (F, 1), (F, 1), (E, 1), (E, 1), (D, 2),
    (C, 1), (C, 1), (G, 1), (G, 1), (A, 1), (A, 1), (G, 2),
    (F, 1), (F, 1), (E, 1), (E, 1), (D, 1), (D, 1), (C, 2),
]

BEAT = 0.4


def light_on():
    board.digital_write(RED_PIN, 1)
    board.digital_write(GREEN_PIN, 1)
    board.digital_write(BLUE_PIN, 1)


def light_off():
    board.digital_write(RED_PIN, 0)
    board.digital_write(GREEN_PIN, 0)
    board.digital_write(BLUE_PIN, 0)


def play_note(frequency, length):
    light_on()
    board.play_tone_continuously(TONE_PIN, frequency)
    time.sleep(BEAT * length * 0.85)

    board.play_tone_off(TONE_PIN)
    light_off()
    time.sleep(BEAT * length * 0.15)


try:
    for frequency, length in SONG:
        play_note(frequency, length)
finally:
    board.play_tone_off(TONE_PIN)
    light_off()
    board.shutdown()
