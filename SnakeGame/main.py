from turtle import Screen, Turtle
from typing import List, Tuple
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('My Snake Game')
screen.tracer(0)  # pauses screen

starting_positions: List[Tuple] = [(0, 0), (-20, 0), (-40, 0)]
segments: list = []

for position in starting_positions:
    snake_segment = Turtle('square')
    snake_segment.color('white')
    snake_segment.penup()
    snake_segment.goto(position)
    segments.append(snake_segment)


def snake_movement(segments):
    screen.tracer(True)
    time.sleep(0.1)
    # Reminder the variable integer becomes the [index_key] when range is in play
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)


game_on: bool = True
while game_on:
    snake_movement(segments)


screen.exitonclick()
