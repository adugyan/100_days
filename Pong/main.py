from turtle import Screen
from scoreboard import ScoreBoard
from paddle import Paddle


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('Pong')
screen.tracer(0)  # pauses screen

p1_paddle = Paddle([(-350, 0)])
scoreboard = ScoreBoard()

# screen.onkey(key='Up', fun=paddle.move_up)
#screen.onkey(key='Down', fun=snake.move_down)
screen.listen()

game_on: bool = True
while game_on:
    screen.update()

screen.exitonclick()