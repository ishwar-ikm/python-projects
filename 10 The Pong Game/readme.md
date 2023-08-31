# Pong Game

This is a classic Pong Game implemented in Python using the Turtle graphics library. The game involves two players controlling paddles to hit a ball back and forth. The objective is to prevent the ball from reaching your side and gain points by hitting the ball past your opponent's paddle.

## How to Play

1. Run the `main.py` file to start the game.
2. Control the left paddle using the `W` (move up) and `S` (move down) keys.
3. Control the right paddle using the `Up Arrow` (move up) and `Down Arrow` (move down) keys.
4. The ball bounces off the top and bottom walls and paddles.
5. The game ends if the ball goes past either paddle.
6. Players' scores are displayed at the top of the screen.

## Project Structure

The project consists of the following Python files:

- `main.py`: Contains the main game loop and logic.
- `ball.py`: Defines the `Ball` class to manage the ball's properties and movement.
- `paddle.py`: Defines the `Paddle` class to manage the paddle's properties and movement.
- `score.py`: Defines the `Score` and `Line` classes to track and display scores.

## Usage

1. Clone the repository to your local machine.
2. Make sure you have Python and the Turtle graphics library installed.
3. Run `main.py` using a Python interpreter.

```bash
python main.py
