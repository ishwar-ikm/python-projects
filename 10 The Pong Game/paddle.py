import turtle


# In the Paddle class, which inherits the Turtle class, the Paddle's properties and behavior are defined
class Paddle(turtle.Turtle):
    def __init__(self, position): # Constructor to define the characteristics of the paddle
        super().__init__() # Calling the constructor from the super class
        self.yCor = 0 # Attribute for y co-ordinate of the paddle
        self.up()
        self.color("white") # Color of paddle set to white
        self.shape("square")
        self.shapesize(stretch_wid=4.5, stretch_len=1) # Define the length of the paddle
        self.goto(position) # Set the initial position of paddle

    # Method to move up the paddle 
    def move_up(self):
        self.yCor -= -20
        self.sety(self.yCor)

    # Method to move down the paddle
    def move_down(self):
        self.yCor += -20
        self.sety(self.yCor)
