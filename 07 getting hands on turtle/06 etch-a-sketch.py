# In this program turtle listens to the user input and act according to it
import turtle

tim = turtle.Turtle()
sc = turtle.Screen()


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


sc.listen()
sc.onkey(key='w', fun=move_forward)
sc.onkey(key='s', fun=move_backward)
sc.onkey(key='a', fun=turn_left)
sc.onkey(key='d', fun=turn_right)
sc.onkey(key='space', fun=tim.reset)
sc.exitonclick()
