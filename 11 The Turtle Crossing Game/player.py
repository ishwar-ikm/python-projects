import turtle


# In the Player class, which inherits Turtle class, the player's properties and behavior are defined
class Player(turtle.Turtle):
    # Constructor to define the appearance and properties of the player 
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(1.7)
        self.up()
        self.goto(0, -270)
        self.setheading(90)

    # Method to move the turtle up
    def move_up(self):
        self.forward(20)

    # Method to move the turtle left
    def move_left(self):
        self.lt(90)
        self.forward(20)
        self.rt(90)

    # Method to move the turtle right
    def move_right(self):
        self.rt(90)
        self.forward(20)
        self.lt(90)

    # Method to reset the turtle position back to the begining
    def restart(self):
        self.goto(0, -270)
