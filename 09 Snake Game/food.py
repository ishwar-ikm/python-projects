import turtle
import random


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.up()
        self.speed(0)
        self.shapesize(0.6)
        self.set_position()

    def set_position(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 255)
        self.goto(x, y)

