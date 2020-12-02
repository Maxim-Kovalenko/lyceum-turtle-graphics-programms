from turtle import *

#За допомогою цієї змінної можна змінювати розміри будинку та дерева
coeficient = 1

speed(10)
shape("turtle")

def base():
    fillcolor("#fae0bd")
    begin_fill()
    pencolor("#c8835c")
    pensize(10 * coeficient)
    penup()
    backward(100 * coeficient)
    pendown()
    for i in range(0,2):
        forward(300 * coeficient)
        right(90)
        forward(200 * coeficient)
        right(90)
    end_fill()


def roof():
    begin_fill()
    fillcolor("#fe8e97")
    pencolor("#fe8e97")
    backward(40 * coeficient)
    left(90)
    forward(50 * coeficient)
    right(90)
    forward(380 * coeficient)
    right(90)
    forward(50 * coeficient)
    right(90)
    forward(40 * coeficient)
    end_fill()

def window():
    penup()
    forward(250 * coeficient)
    left(90)
    forward(50 * coeficient)
    pendown()
    fillcolor("#87d5e0")
    pencolor("#87d5e0")
    begin_fill()
    for f in range(0,4):
        forward(90 * coeficient)
        left(90)
    end_fill()

def door():
    penup()
    left(90)
    forward(150 * coeficient)
    pendown()
    pencolor("#de692e")
    fillcolor("#de692e")
    begin_fill()
    for v in range(0,2):
        forward(50 * coeficient)
        right(90)
        forward(130 * coeficient)
        right(90)
    end_fill()    

def move():
    penup()
    goto(400 * coeficient,0)
    pendown()

def tree_trunk():
    fillcolor("#b56f2f")
    pencolor("#b56f2f")
    begin_fill()
    for m in range(0,2):
        forward(30 * coeficient)
        right(90)
        forward(200 * coeficient)
        right(90)
    end_fill()
def leaves_1():
    forward(15 * coeficient)
    pencolor("#9acc58")
    fillcolor("#9acc58")
    begin_fill()
    circle(90 * coeficient)
    end_fill()
    penup()
    right(40)
    forward(40*coeficient)
    left(90)
    forward(15*coeficient)
    right(90)
    pendown()
def leaves_2():
    pencolor("#68a63a")
    fillcolor("#68a63a")
    begin_fill()
    circle(70 * coeficient)
    end_fill()
    pencolor("#435037")
    right(135)
    penup()
    forward(50*coeficient)
    right(100)
    forward(10*coeficient)
    pendown()
def leaves_3():
    fillcolor("#435037")
    begin_fill()
    circle(70* coeficient)
    end_fill()
    


base()
roof()
window()
door()
move()
tree_trunk()
leaves_1()
leaves_2()
leaves_3()


