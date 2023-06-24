import turtle, random

# Making an object for Screen and setting its width and height
sc = turtle.Screen()
sc.setup(width=500, height=500)


# Getting the user's bet and checking if the user entered the color from the given list
color = ["red", "purple", "green", "blue", "yellow", "orange"]
while True:
    bet = sc.textinput(title="Color bet", prompt="Select Which color to bet on")
    if bet in color:
        break


# Creating a list called  tim to store 6 Turtle objects and setting y for adjusting the co-ordinates fir the turtle
tim = []
y = -120


# Using a for loop we created 6 turtle objects and simultaneously setting it's properties as desired
for i in range(6):
    tim.append(turtle.Turtle(shape="turtle"))
    tim[i].shapesize(1.7)
    tim[i].color(color[i])
    tim[i].up()
    tim[i].goto(-220, y)
    y += 50


# Function that takes a random j value for which turtle to move and randomly setting its speed for movement
def race_move(j):
    tim[j].speed(random.randint(0, 10))
    tim[j].forward(5)


# Randomly selecting a turtle index in temp and calling the race_move function in an endless loop
# Every iteration, we check if the chosen turtle has reached the final end point, and if any turtle has reached the end point, we break the loop.
win = "abc"
while True:
    temp = random.randint(0, 5)
    race_move(temp)
    if tim[temp].pos() >= (245, tim[temp].ycor()):
        win = color[temp]
        break


# Checking if the user's chosen turtle won or not
if bet == win:
    print("Congratulations! Your Turtle won the race.")
else:
    print(f"Sorry! The winner is {win} Turtle.")

sc.exitonclick()
