from turtle import *


def move(xstart, ystart):
    penup()
    goto(xstart, ystart)
    pendown()


def replace_pos(x, y):
    penup()
    goto(int(xcor()) + x, int(ycor()) + y)
    pendown()


def move_and_paint(x, y):
    goto(int(xcor()) + x, int(ycor()) + y)


def polygon(num_count, side, color1, color2):
    pencolor(color1)
    fillcolor(color2)
    begin_fill()
    for count in range(num_count):
        left(360/num_count)
        forward(side)
    end_fill()


def frame(height):
    pensize(5)
    pencolor("brown")
    x = height / 2
    replace_pos(x * 1.5, 0)
    move_and_paint(0, x)
    move_and_paint(x * -3, 0)
    move_and_paint(0, x * -2)
    move_and_paint(x * 3, 0)
    move_and_paint(0, x)
    replace_pos(-2 * x, -x)


def square(side, color1, color2):
    pensize(1)
    begin_fill()
    polygon(4, side, color1, color2)
    end_fill()


def triangle(side, color1, color2):
    penup()
    forward(side/10)
    pendown()
    pensize(3)
    begin_fill()
    polygon(3, side + side/5, color1, color2)
    end_fill()


def window(side):
    penup()
    backward(side/10)
    right(90)
    forward(side/10)
    right(90)
    forward(side/10)
    pendown()
    polygon(4, side/8, "black", "cyan")


def base(size):
    penup()
    left(90)
    pendown()
    right(90)
    square(size, "brown", "darkorange")
    replace_pos(0, size)
    triangle(size, "brown", "yellow")


def house_line(count, side):
    for c in range(count):
        base(side/4)
        window(side)
        penup()
        backward(side)
        pendown()
        left(180)


def picture(height, xstart, ystart, forwardHeight):
    move(xstart, ystart)
    frame(height)
    left(90)
    penup()
    forward(forwardHeight)
    pendown()
    right(90)
    house_line(2, height)


speed(int(input("Уведіть швидкість малювання: ")))
side_for_picture = int(input("уведіть довжину від якої залежить height та width: "))
xstart = int(input("уведіть початковий X: "))
ystart = int(input("уведіть початковий Y: "))
picture(side_for_picture, xstart, ystart, side_for_picture/5)
#polygon(3, 70)
#picture(400, 0, 0, )
#triangle(100, "blue", "cyan")