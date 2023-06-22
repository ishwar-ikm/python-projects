#This code was to extract colors from the image called hirst_img.jpg
# import colorgram
#
# color = colorgram.extract('hirst_img.jpg', 35)
#
# for i in range(35):
#     color[i] = tuple(color[i].rgb)
#
# print(color)

color = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]

import turtle, random

tim = turtle.Turtle()
tim.speed(0)
tim.up()
tim.hideturtle()
sc = turtle.Screen()
sc.colormode(255)

y = -225
tim.goto(-225, -225)

for i in range(10):
    for j in range(10):
        tim.dot(20, random.choice(color))
        tim.forward(50)
    y += 50
    tim.goto(-225, y)


sc.exitonclick()