import turtle


class Snake:
    body = []

    def __init__(self):
        x = 0
        pos = (x, 0)
        for i in range(3):
            self.add_tail(pos)
            x -= 20
        self.head = self.body[0]

    def add_tail(self, position):
        tail = turtle.Turtle(shape="square")
        tail.color("white")
        tail.up()
        tail.goto(position)
        self.body.append(tail)

    def extend(self):
        self.add_tail(self.body[-1].position())

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].goto(self.body[i - 1].pos())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
