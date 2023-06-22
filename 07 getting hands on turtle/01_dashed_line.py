from turtle import *

tim = Turtle()

for i in range(15):
    tim.forward(10)
    tim.up()
    tim.forward(10)
    tim.down()

sc = Screen()
sc.exitonclick()