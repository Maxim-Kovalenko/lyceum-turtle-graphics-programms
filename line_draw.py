from turtle import *
from random import *

a = 1

def f(x,y):
    colors = ["green", "blue", "lime", "orange", "violet", "pink", "black", "yellow", "red"]
    pencolor(choice(colors))
    goto(x,y)
def f1(x, y):
    global a
    a = a+1
    pensize(a)

def f2(x, y):
    global a
    a = a+1
    speed(a)

onscreenclick(f, 1)
onscreenclick(f1, 2)
onscreenclick(f2, 3)
