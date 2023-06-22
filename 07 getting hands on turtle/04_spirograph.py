import random, turtle

tim = turtle.Turtle()
sc = turtle.Screen()
tim.speed(0)
sc.colormode(255)


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color(r, g, b)


def make():
    change_color()
    tim.circle(100)
    tim.lt(5)


for _ in range(72):
    make()

sc.exitonclick()