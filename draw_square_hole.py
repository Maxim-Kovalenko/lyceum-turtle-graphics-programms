import turtle
import random
chin = turtle.Turtle()
d = 10
chin.speed(10)
chin.shape("turtle")
colours = ["red", "yellow", "dark orchid", "aquamarine", "cyan", "goldenrod", "lime green", "hot pink"]
def black_hole():
    for i in range(0, 4):
        chin.forward(d)
        chin.left(90)
    chin.color(random.choice(colours))
    chin.left(20)
while True:
    black_hole()
    d = d + 4