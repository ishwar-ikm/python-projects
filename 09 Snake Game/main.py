import turtle
import time
import food
import scoreboard
from snake import Snake

sc = turtle.Screen()
sc.setup(width=600, height=600)
sc.title("My Snake Game")
sc.bgcolor("black")
sc.tracer(0)

snake = Snake()
food = food.Food()
score = scoreboard.Score()

sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.right, "Right")
sc.onkey(snake.left, "Left")
sc.onkey(snake.up, "W")
sc.onkey(snake.down, "S")
sc.onkey(snake.right, "D")
sc.onkey(snake.left, "A")
sc.onkey(snake.up, "w")
sc.onkey(snake.down, "s")
sc.onkey(snake.right, "d")
sc.onkey(snake.left, "a")


game_continue = True
while game_continue:
    sc.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.set_position()
        snake.extend()
        score.inc_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 255 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        score.game_over()
        game_continue = False

    # detect colision with body
    for body in snake.body:
        if body == snake.head:
            continue
        elif snake.head.distance(body) < 10:
            score.game_over()
            game_continue = False


sc.exitonclick()
