import turtle
import paddle
import time
import ball
import score


sc = turtle.Screen()
sc.tracer(0)
sc.title("The Pong Game")
sc.bgcolor("black")
sc.setup(width=1000, height=600)


left = paddle.Paddle((-470, 0))
right = paddle.Paddle((470, 0))
ball = ball.Ball()
scoreLeft = score.Score((-50, 240))
scoreRight = score.Score((30, 240))
line = score.Line()


sc.listen()
sc.onkey(left.move_up, "w")
sc.onkey(left.move_down, "s")
sc.onkey(left.move_up, "W")
sc.onkey(left.move_down, "S")
sc.onkey(right.move_up, "Up")
sc.onkey(right.move_down, "Down")


while True:
    sc.update()
    time.sleep(0.0001)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(left) < 40 and ball.xcor() < -360 or ball.distance(right) < 40 and ball.xcor() > 360:
        ball.bounce_x()

    if ball.xcor() > 490:
        scoreLeft.update()
        ball.reset()

    if ball.xcor() < -490:
        scoreRight.update()
        ball.reset()
