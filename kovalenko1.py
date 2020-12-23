from turtle import *
import time

# from random import *
def move(x, y):
    penup()
    goto(x, y)
    pendown()


def fillpolygon(side, count, color1, color2):
    pencolor(color2)
    fillcolor(color1)
    begin_fill()
    for i in range(count):
        forward(side)
        left(360 / count)
    end_fill()


def christmas_tree(size, xStart, yStart):
    move(xStart, yStart)
    fillpolygon(size, 4, "brown", "black")
    left(90)
    forward(size)
    right(90)
    backward(size)
    for g in range(2):
        fillpolygon(size * 3, 3, "lightgreen", "green")
        left(60)
        forward(size * 2)
        right(60)
        backward(size)
    fillpolygon(size * 3, 3, "lightgreen", "green")
    '''left(60)
    forward(size*3)
    right(60)
    backward(size/4)
    fillpolygon(size/2, 5, "orange", "darkorange")'''


def treesLine(side, minX, y, count, distBetw):
    for counter in range(count):
        x = minX + distBetw * counter
        christmas_tree(side, x, y)


def star(side, mainColor, fillColor, x, y):
    move(x, y)
    pencolor(mainColor)
    fillcolor(fillColor)
    begin_fill()
    left(107)
    for count in range(5):
        forward(side)
        left(144)
    penup()
    right(107)
    end_fill()


def starLine(side, minX, y, count, distBetw):
    for counter in range(count):
        x = minX + distBetw * counter
        star(side, "yellow", "yellow", x, y)

def frame(x1, y1, x2, y2, color):
    pensize(10)
    pencolor(color)
    move(x1, y1)
    goto(x1, y2)
    goto(x2, y2)
    goto(x2, y1)
    goto(x1, y1)

'''def writeline(line, color):
    pencolor(color)
    left(90)
    penup()
    forward(55)
    left(90)
    forward(30)
    write(line)'''

bgcolor("cyan")
speed(2)
pensize(3)

'''
starLine(40, -900, 500, 15, 120)
starLine(40, -900, 380, 13, 150)
starLine(40, -900, 300, 15, 120)
treesLine(20, -900, 100, 23, 80)
treesLine(20, -700, -100, 18, 80)
treesLine(20, -900, -300, 23, 80)
#'''

frame(-950, -590, 500, 575, "darkorange")
# writeline("Merry Christmas!", "darkblue")
