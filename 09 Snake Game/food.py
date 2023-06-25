import turtle
import random


# Create a food class
class Food(turtle.Turtle):

    # Define the constructor for the appearance of the food
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.up()
        self.speed(0)
        self.shapesize(0.6)
        self.set_position()

    # Method to randomly set the position of the food
    def set_position(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 255)
        self.goto(x, y)
