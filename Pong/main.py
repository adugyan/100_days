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
    time.sleep((0.1))
    screen.update()
    ball.move()

screen.exitonclick()