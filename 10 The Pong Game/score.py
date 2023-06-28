import turtle


# In the Score class, which inherits the Turtle class, the score of both the players are tracked
class Score(turtle.Turtle):

    # Constructor to define the text properties
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.score = 0
        self.display()

    # Method to display the text
    def display(self):
        self.write(f"{self.score}", font=("Arial", 30, "normal"))

    # Method to update the score and refresh the score
    def update(self):
        self.score += 1
        self.clear()
        self.display()


# In the Line class, which inherits the Turtle class, the Line's properties are defined
class Line(turtle.Turtle):

    # Constructor to define the propertied of the line as well as to make the line
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 300)
        self.setheading(270)
        self.pendown()
        self.pensize(3)
        # Below code will make the dotted lines in between
        for _ in range(15):
            self.forward(20)
            self.up()
            self.forward(20)
            self.down()
