from turtle import *
from random import *


def move(xstart, ystart):
    penup()
    goto(xstart, ystart)
    pendown()


def moveDelta(x, y):
    penup()
    goto(int(xcor()) + x, int(ycor()) + y)
    pendown()


def moveDeltaAndPaint(x, y):
    goto(int(xcor()) + x, int(ycor()) + y)


def frame(height):
    pensize(5)
    pencolor("brown")
    x = height / 2
    moveDelta(x * 1.5, 0)
    moveDeltaAndPaint(0, x)
    moveDeltaAndPaint(x * -3, 0)
    moveDeltaAndPaint(0, x * -2)
    moveDeltaAndPaint(x * 3, 0)
    moveDeltaAndPaint(0, x)
    moveDelta(-2 * x, -x)


def square(side):
    pensize(1)
    pencolor(choice(["green", "blue", "yellow"]))
    fillcolor(choice(["green", "blue", "yellow"]))
    begin_fill()
    moveDeltaAndPaint(side, 0)
    moveDeltaAndPaint(0, side)
    moveDeltaAndPaint(-side, 0)
    moveDeltaAndPaint(0, -side)
    end_fill()


def triangle(side):
    pensize(3)
    pencolor(choice(["green", "blue", "yellow"]))
    fillcolor(choice(["green", "blue", "yellow"]))
    begin_fill()
    forward(side)
    left(120)
    forward(side)
    left(120)
    forward(side)
    left(120)
    end_fill()


def house(size, forwardHeight):
    penup()
    left(90)
    forward(forwardHeight)
    pendown()
    right(90)
    square(size)
    moveDelta(0, size)
    triangle(size)


def picture(height, xstart, ystart):
    move(xstart, ystart)
    frame(height)
    house(height / 4, height / 4)


speed(5)
picture(int(input("Введіть висоту вашого зображення: ")), int(input("Уведіть початковий X: ")), int(input("Уведіть початковий Y: ")))

