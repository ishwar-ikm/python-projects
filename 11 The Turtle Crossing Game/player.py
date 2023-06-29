import turtle


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(1.7)
        self.up()
        self.goto(0, -270)
        self.setheading(90)

    def move_up(self):
        self.forward(20)

    def move_left(self):
        self.lt(90)
        self.forward(20)
        self.rt(90)

    def move_right(self):
        self.rt(90)
        self.forward(20)
        self.lt(90)

    def restart(self):
        self.goto(0, -270)