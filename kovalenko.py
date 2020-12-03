from turtle import *

def sea(sea_side1, sea_side2):
    speed(5)
    pensize(5)
    pencolor("lightblue")
    fillcolor("lightblue")
    begin_fill()
    forward(sea_side1)
    backward(sea_side1*2)
    right(90)
    forward(sea_side2)
    left(90)
    forward(sea_side1*2)
    left(90)
    forward(sea_side2)
    end_fill()
    
def boat():
    pensize(10)
    pencolor("brown")
    fillcolor("brown")
    home()
    forward(50)
    backward(100)
    left(135)
    forward(50)
    

shape("turtle")
sea(1000,1000)
boat()
