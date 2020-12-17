from turtle import *
#from random import *
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
def treesline(side, minX, y, count, distBetw):
    for counter in range(count):
        x = minX + distBetw * counter
        christmas_tree(side, x, y)
        
    
'''def writeline(line, color):
    pencolor(color)
    left(90)
    penup()
    forward(55)
    left(90)
    forward(30)
    write(line)'''

bgcolor("cyan")
speed(0)
pensize(3)
treesline(20, -900, 100, 23, 80)
treesline(20, -700, -100, 18, 80)
treesline(20, -900, -300, 23, 80)
#writeline("Merry Christmas!", "darkblue")
