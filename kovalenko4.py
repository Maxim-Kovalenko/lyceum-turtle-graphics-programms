from turtle import *
from random import *


def changeColor(x, y):
    bgcolor(choice(['red', 'yellow', 'green', 'blue',
                    'white', 'black', 'orange', 'pink']))


onscreenclick(changeColor)