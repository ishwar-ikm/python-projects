import turtle, random

tim = turtle.Turtle()
tim.speed(5)
tim.pensize(10)
sc = turtle.Screen()
sc.colormode(255)
direction = [0, 90, 180, 270]


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color(r, g, b)


def move():
    tim.lt(random.choice(direction))
    tim.forward(30)


for i in range(200):
    change_color()
    move()

sc.exitonclick()
