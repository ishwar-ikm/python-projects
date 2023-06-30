import turtle
import time

# Create a class score to update and keep track for the score
class Score(turtle.Turtle):

    # Define the constructor for the appearance of score board and its position
    def __init__(self):
        super().__init__()
        with open("high_score_data.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.up()
        self.hideturtle()
        self.display()

    # Method to display the score
    def display(self):
        self.goto(0, 260)
        self.clear()
        self.write(f"Score = {self.score}", align="center", font=("Arial", 24, "normal"))

    # Method to update the score
    def inc_score(self):
        self.score += 1
        self.display()

    # Method to display game over sequence and clear it after some ttme to reset the game to play again
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 20, "normal"))
        time.sleep(0.5)  # Wating for some time to clear the screen and restart the game
        self.clear()

    # Method to reset the game back to the begining
    def reset(self):
        if self.score > self.high_score:
            with open("high_score_data.txt", mode="w") as file:
                file.write(f"{self.score}")
                self.high_score = self.score
        self.score = 0
        self.game_over()
        self.display()
