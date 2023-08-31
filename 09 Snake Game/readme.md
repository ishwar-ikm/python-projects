# Snake Game

This is a classic Snake Game implemented in Python using the Turtle graphics library. The game involves controlling a snake that must collect food to grow longer. The game ends if the snake hits the wall or collides with its own body.

## How to Play

1. Run the `main.py` file to start the game.
2. Control the snake's movement using the arrow keys (Up, Down, Left, Right) or the keys (W, A, S, D).
3. The snake's goal is to eat the food that appears on the screen.
4. Each time the snake eats food, it grows longer, and your score increases.
5. The game ends if the snake hits the wall or collides with its own body.

## Project Structure

The project consists of the following Python files:

- `main.py`: Contains the main game loop and logic.
- `food.py`: Defines the `Food` class to manage food's properties and position.
- `scoreboard.py`: Defines the `Score` class to manage the player's score and display.
- `snake.py`: Defines the `Snake` class to manage the snake's behavior and body.
- `high_score_data.txt`: Stores the highest score achieved on the local machine.

## Usage

1. Clone the repository to your local machine.
2. Make sure you have Python and the Turtle graphics library installed.
3. Run `main.py` using a Python interpreter.

```bash
python main.py
