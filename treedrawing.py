from turtle import *

def move(x, y):
    penup()
    goto(x, y)
    pendown()
    
def fillpolygon(side, count, color):
    pencolor(color)
    fillcolor(color)
    begin_fill()
    for i in range(count):
        forward(side)
        left(360/count)
    end_fill()
    
def christmass_tree(size, xStart, yStart):
    move(xStart, yStart)
    fillpolygon(size, 4, "brown")
    left(90)
    forward(size)
    right(90)
    pencolor("lightgreen")
    backward(size)
    fillpolygon(size*3, 3, "lightgreen")
    left(60)
    forward(size*2)
    right(60)
    backward(size)
    fillpolygon(size*3, 3, "lightgreen")

speed(1)
christmass_tree(30 ,0, 0)
