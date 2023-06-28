import turtle


class Score(turtle.Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.score = 0
        self.display()

    def display(self):
        self.write(f"{self.score}", font=("Arial", 30, "normal"))

    def update(self):
        self.score += 1
        self.clear()
        self.display()


class Line(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 300)
        self.setheading(270)
        self.pendown()
        self.pensize(3)
        for _ in range(15):
            self.forward(20)
            self.up()
            self.forward(20)
            self.down()