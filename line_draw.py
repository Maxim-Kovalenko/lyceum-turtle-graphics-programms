from turtle import *
from random import *

a = 1

def drawLine(x,y):
    colors = ["green", "blue", "lime", "orange", "violet", "pink", "black", "yellow", "red"]
    pencolor(choice(colors))
    goto(x,y)
def increasePenSize(x, y):
    global a
    a = a+1
    pensize(a)

def increaseSpeed(x, y):
    global a
    a = a+1
    speed(a)

onscreenclick(drawLine, 1)
onscreenclick(increasePenSize, 2)
onscreenclick(increaseSpeed, 3)
