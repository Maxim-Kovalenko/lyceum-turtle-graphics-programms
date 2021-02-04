from turtle import *
from random import *


def drawLine(x,y):
    colors = ["green", "blue", "lime", "orange", "violet", "pink", "black", "yellow", "red"]
    pencolor(choice(colors))
    goto(x,y)
    write(format(position()))
    

def move(x, y):
    penup()
    goto(x, y)
    pendown()


def polygon(x, y):
    count = randint(3, 10)
    side = randint(10, 80)
    for i in range(count):
        forward(side)
        left(360 / count)
    end_fill()


onscreenclick(drawLine, 1)
onscreenclick(move, 3)
onscreenclick(polygon, 2)
 
