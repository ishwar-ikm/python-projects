import turtle


class ScoreBoards(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.color("black")
        self.level = 0

    def game_over(self):
        self.goto(0, 0)
        self.write(f"    Game Over\nYour score was {self.level}", align='center', font=("Arial", 20, 'normal'))

    def level_inc(self):
        self.level += 1
        self.clear()
        self.goto(-380, 250)
        self.write(f"Level - {self.level}", font=("Arial", 30, 'normal'))