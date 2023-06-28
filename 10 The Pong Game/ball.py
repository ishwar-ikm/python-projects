import time
import turtle


# In the Ball class, which inherits the Turtle class, the ball's properties and behavior are defined
class Ball(turtle.Turtle):

    # Constructor to define the properties of the ball
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.x = 3
        self.y = 3

    # Method to move the ball
    def move(self):
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        self.goto(x, y)

    # Method to bounce the ball with the upper wall and lower wall by changing the y attribute
    def bounce_y(self):
        self.y *= -1

    # Method to bounce the ball with the paddle by changing the x attribute
    def bounce_x(self):
        self.x *= -1

    # Method to reset the ball to original place to start another round
    def reset(self):
        self.goto(0, 0)
        time.sleep(1)
