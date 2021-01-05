from turtle import *

def movedelta(x, y):
    penup()
    goto(int(xcor()) + x, int(ycor()) + y)
    pendown()

def movedeltaandpaint(x, y):
    goto(int(xcor()) + x, int(ycor()) + y)

def frame(height):
    x = height / 2
    movedelta(x * 1.5, 0)
    movedeltaandpaint(0, x)
    movedeltaandpaint(x * -3, 0)
    movedeltaandpaint(0, x * -2)
    movedeltaandpaint(x * 3, 0)
    movedeltaandpaint(0, x)
    movedelta(-2 * x, -x)

def square(side):
    movedeltaandpaint(side, 0)
    movedeltaandpaint(0, side)
    movedeltaandpaint(-side, 0)
    movedeltaandpaint(0, -side)

def triangle(side):
    forward(side)
    left(120)
    forward(side)
    left(120)
    forward(side)
    left(120)

def house(size):
    square(size)
    movedelta(0, size)
    triangle(size)

def picture(height):
    frame(height)
    house(height / 2)

print("Please enter the height of your picture, preferably even")
picture(int(input()))

