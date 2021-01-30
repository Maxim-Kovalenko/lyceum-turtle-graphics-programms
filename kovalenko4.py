from turtle import *
from random import *

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
    
def flowerOnClick(x, y):
    petal_color = choice(['red', 'green', 'blue',
                     'orange', 'pink'])
    petal_size = randint(30, 70)
    stem_color = choice(['lime', 'green'])
    flower(petal_color, petal_size, 'yellow', stem_color)

    
onscreenclick(flowerOnClick, 1)
 
