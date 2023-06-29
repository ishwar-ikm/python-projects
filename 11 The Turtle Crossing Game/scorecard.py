import turtle


# In the ScoreBoards class, which inherits Turtle class, the player's score is tracked and displayed
class ScoreBoards(turtle.Turtle):
    # Constructor to set the color of the text and other attributes
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.color("black")
        self.level = 0  # level attribute to keep track of the level

    # Method to show the game over text and the score player scored
    def game_over(self):
        self.goto(0, 0)
        self.write(f"    Game Over\nYour score was {self.level}", align='center', font=("Arial", 20, 'normal'))

    # Method increment the level attribute and display the level on the screen
    def level_inc(self):
        self.level += 1
        self.clear()
        self.goto(-380, 250)
        self.write(f"Level - {self.level}", font=("Arial", 30, 'normal'))
