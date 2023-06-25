import turtle

# Create a class score to update and keep track for the score
class Score(turtle.Turtle):

    # Define the constructor for the appearance of score board and its position
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.up()
        self.hideturtle()
        self.goto(0, 260)
        self.display()

    # Method to display the score
    def display(self):
        self.write(f"Score = {self.score}", align="center", font=("Arial", 24, "normal"))

    # Method to update the score
    def inc_score(self):
        self.score += 1
        self.clear()
        self.display()

    # Method to display game over sequence
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 20, "normal"))
