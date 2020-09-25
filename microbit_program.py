from microbit import *
import random

while True:
    if accelerometer.was_gesture('shake'):
        display.scroll(random.randint(2, 12))