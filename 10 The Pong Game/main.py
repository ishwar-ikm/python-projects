# import all the files need
import turtle
import paddle
import time
import ball
import score


# sc object to define the properties of screen required
sc = turtle.Screen()
sc.tracer(0)
sc.title("The Pong Game")
sc.bgcolor("black")
sc.setup(width=1000, height=600)


left = paddle.Paddle((-470, 0)) # left object for the left paddle
right = paddle.Paddle((470, 0)) # left object for the left paddle
ball = ball.Ball() # ball object for the properties of the ball
scoreLeft = score.Score((-50, 240)) # scoreLeft object keeps track of the left player's score
scoreRight = score.Score((30, 240)) # scoreRight object keeps track of the right player's score
line = score.Line() # Line object to make a middle line between both the players


# Listeners for the user input
sc.listen()
sc.onkey(left.move_up, "w")
sc.onkey(left.move_down, "s")
sc.onkey(left.move_up, "W")
sc.onkey(left.move_down, "S")
sc.onkey(right.move_up, "Up")
sc.onkey(right.move_down, "Down")


while True:
    sc.update()
    time.sleep(0.0001) # To keep track of the speed
    ball.move() # move method from ball class to move the ball

    if ball.ycor() > 280 or ball.ycor() < -280: # Detect the collision of from the top and bottom line to bounce it back
        ball.bounce_y() # bounce_y method to bouce the ball

    if ball.distance(left) < 40 and ball.xcor() < -360 or ball.distance(right) < 40 and ball.xcor() > 360: # Detect the collision of from the paddle to bounce it back
        ball.bounce_x() # bounce_x method to bouce the ball from the paddle

    if ball.xcor() > 490:  # Condition to check whether right player missed the ball or not
        scoreLeft.update() # If missed, update the left player's score
        ball.reset() # Reset the ball to continue the game again

    if ball.xcor() < -490: # Condition to check whether left player missed the ball or not
        scoreRight.update() # If missed, update the right player's score
        ball.reset() # Reset the ball to continue the game again
