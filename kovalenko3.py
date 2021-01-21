from turtle import *
import random


def move(x, y):
    penup()
    goto(x, y)
    pendown()


def fillpolygon(side, count, fill_color, pen_color):
    pencolor(pen_color)
    fillcolor(fill_color)
    begin_fill()
    for i in range(count):
        forward(side)
        left(360 / count)
    end_fill()


def flower(petal_color, petal_size, center_color, stem_color):
    pensize(3)
    pencolor(stem_color)
    right(90)
    forward(petal_size*2)
    back(petal_size*2)
    left(60)
    for count in range(5):
        fillpolygon(petal_size, 3, petal_color, petal_color)
        right(360/5)
    dot(petal_size, center_color)


def flower_lay(min_x, max_x, min_y, max_y, min_petal_size, max_petal_size, count):
    for c in range(count):
        x = random.randint(min_x, max_x)
        y = random.randint(min_y, max_y)
        petal_size = random.randint(min_petal_size, max_petal_size)
        move(x, y)
        flower("pink", petal_size, "yellow", "green")


flower_lay(400, -400, 400, -400, 30, 60, 12)


