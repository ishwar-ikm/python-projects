import turtle


class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.yCor = 0
        self.up()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=4.5, stretch_len=1)
        self.goto(position)

    def move_up(self):
        self.yCor -= -20
        self.sety(self.yCor)

    def move_down(self):
        self.yCor += -20
        self.sety(self.yCor)