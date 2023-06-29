import turtle
import random


class Car:
    def __init__(self):
        self.SPEED = 3
        self.num_car = 10
        self.all_car = []
        sc = turtle.Screen()
        sc.colormode(255)

    def create_car(self):
        ran = random.randint(1, self.num_car)
        if ran == 1:
            new_car = turtle.Turtle()
            new_car.shape("square")
            new_car.up()
            new_car.shapesize(stretch_len=3, stretch_wid=1.5)
            new_car.setheading(180)
            self.random_color(new_car)
            self.random_coordinate(new_car)
            self.all_car.append(new_car)

    def random_color(self, new_car):
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        new_car.color(a, b, c)

    def random_coordinate(self, new_car):
        y = random.randint(-200, 200)
        new_car.goto(430, y)

    def move(self):
        for car in self.all_car:
            car.forward(self.SPEED)

    def inc_speed(self):
        self.SPEED += 2
        self.num_car -= 1
