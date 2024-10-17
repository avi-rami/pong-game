from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(x_cor=350)
left_paddle = Paddle(x_cor=-360)
ball = Ball()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(key="Up", fun=right_paddle.move_paddle_up)
screen.onkey(key="Down", fun=right_paddle.move_paddle_down)
screen.onkey(key="w", fun=left_paddle.move_paddle_up)
screen.onkey(key="s", fun=left_paddle.move_paddle_down)

game_on = True
while game_on is True:
    time.sleep(.01)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    # detect collision with right paddle
    if ball.xcor() > 320 and right_paddle.distance(ball) <= 50:
        ball.bounce_x()

    # detect collision with left paddle
    if ball.xcor() < -330 and left_paddle.distance(ball) <= 50:
        ball.bounce_x()

    # detect if right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_score += 1

    # detect if left paddle misses
    if ball.xcor() < -385:
        ball.reset_position()
        scoreboard.right_score += 1

    # display score
    scoreboard.display_score()

screen.exitonclick()