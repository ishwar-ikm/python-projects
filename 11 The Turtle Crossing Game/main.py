# Importing all the files needed for the project
import time
import turtle
import player
import car
import scorecard


# Setting up the screen size and title
sc = turtle.Screen()
sc.setup(width=800, height=600)
sc.title("The Turtle Crossing Game")
sc.tracer(0)


# Creating objects from the user defined classes
user = player.Player()  # user object to control the behavior of player(turtle)
cars = car.Car()  # cars object to control the behavior of cars
score = scorecard.ScoreBoards()  # score object to display the score
score.level_inc()


# Adding action listener
sc.listen()
sc.onkey(user.move_up, "w")
sc.onkey(user.move_up, "W")
sc.onkey(user.move_up, "Up")
sc.onkey(user.move_left, "a")
sc.onkey(user.move_left, "Left")
sc.onkey(user.move_left, "A")
sc.onkey(user.move_right, "d")
sc.onkey(user.move_right, "Right")
sc.onkey(user.move_right, "D")


# The loop is to make some cars visible before the game starts
for _ in range(250):
    cars.create_car()
    cars.move()


# Game loop
game_on = True
while game_on:
    time.sleep(0.05)  # Controlling the speed of the game
    sc.update()  # Refresh screen after every iteration
    cars.create_car()  # Calling create_car() method to create the car on the screen
    cars.move()  # move() method to move the car horizontally

    # Detect Collision with car
    for car in cars.all_car:
        if car.distance(user) < 35:
            score.game_over()
            game_on = False

    # Detect if the turtle crossed the road
    if user.ycor() > 265:
        score.level_inc()  # Increment the game level
        user.restart()  # restart() method is to reset the turtle back to the starting point to go again
        cars.inc_speed()  # Increases the speed of the car after every level

sc.exitonclick()