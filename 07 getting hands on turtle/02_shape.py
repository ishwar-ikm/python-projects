from turtle import *
import random

tim = Turtle()
sc = Screen()
sc.colormode(255)


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color(r, g, b)


def move(num, angle):
    for j in range(num):
        tim.forward(100)
        tim.right(angle)


for i in range(3, 11):
    change_color()
    move(i, 360/i)


sc.exitonclick()
