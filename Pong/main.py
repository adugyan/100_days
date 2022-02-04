import time
from turtle import Screen
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('Pong')
screen.tracer(0)  # pauses screen

p1_paddle = Paddle((-350, 0))
p2_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.onkey(key='w', fun=p1_paddle.move_up)
screen.onkey(key='s', fun=p1_paddle.move_down)
screen.onkey(key='Up', fun=p2_paddle.move_up)
screen.onkey(key='Down', fun=p2_paddle.move_down)
screen.listen()

game_on: bool = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(p2_paddle) < 50 and ball.xcor() > 320 or ball.distance(p1_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if p2 has been scored on
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.p1_point()

    # Detect if p1 has been scored on
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.p2_point()

screen.exitonclick()
