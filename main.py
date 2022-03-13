# shoot the fruit game (confusing) and with more info by yara

import pgzrun
from random import randint
from pgzero.builtins import *

apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")


def draw():
    screen.clear()
    apple.draw()
    pineapple.draw()
    orange.draw()


def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)


def place_orange():
    orange.x = randint(10, 800)
    orange.x = randint(10, 800)


def place_pineapple():
    pineapple.x = randint(10, 800)
    pineapple.x = randint(10, 800)


def on_mouse_down(pos):
    if pineapple.collidepoint(pos):
        print("Good shot!")
        place_apple()
        place_orange()
        place_pineapple()
    else:
        print("sorry ... not sorry !!! You missed the pineapple!")
        quit()


place_apple()
place_orange()
place_pineapple()
pgzrun.go()
# end of code 11.03.22
