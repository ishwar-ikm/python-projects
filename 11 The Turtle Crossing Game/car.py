import turtle
import random


# In the Car class the car's properties and behavior are defined
class Car:
    # Constructor to create attribute list for all the cars and screen instance to set the color mode to 255 to use rgb type coloring of turtle
    def __init__(self):
        self.SPEED = 3
        self.num_car = 10
        self.all_car = []
        sc = turtle.Screen()
        sc.colormode(255)

    # Method to Create car
    def create_car(self):
        ran = random.randint(1, self.num_car)  # Generating a random number so that car is only created when the ran = 1 and not every time the method is called to avoid overcrowding of cars.
        # Creating a new car and setting its properties
        if ran == 1:
            new_car = turtle.Turtle()
            new_car.shape("square")
            new_car.up()
            new_car.shapesize(stretch_len=3, stretch_wid=1.5)
            new_car.setheading(180)
            self.random_color(new_car)
            self.random_coordinate(new_car)
            self.all_car.append(new_car)  # Appending the new car into the car list

    # Method to generate a random color for the car
    def random_color(self, new_car):
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        new_car.color(a, b, c)

    # Method to randomly set its initial starting position
    def random_coordinate(self, new_car):
        y = random.randint(-200, 200)
        new_car.goto(430, y)

    # Method to move all the cars present in the list
    def move(self):
        for car in self.all_car:
            car.forward(self.SPEED)

    # Method to increase the speed of the car
    def inc_speed(self):
        self.SPEED += 2
        self.num_car -= 1
