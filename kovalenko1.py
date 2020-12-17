from turtle import *
import time

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


def christmass_tree(size, xStart, yStart):
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
    left(60)
    forward(size*3)
    right(60)
    backward(size/4)
    fillpolygon(size/2, 5, "orange", "darkorange")
def writeline(line, color):
    pencolor(color)
    left(90)
    penup()
    forward(55)
    write(line)


speed(5)
pensize(3)
christmass_tree(30, 0, 0)
writeline("Merry Christmas!", "darkblue")

