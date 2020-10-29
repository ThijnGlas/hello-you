from microbit import *
import random
#dobbelsteen
while True:
    if accelerometer.was_gesture('shake'):
        display.scroll(random.randint(2, 12))


#magic 8 ball
answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it"
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]

while True:
    display.show("8")
    if input.button_is_pressed(Button.A):
        display.clear()
        display.scroll(random.choice(answers))
