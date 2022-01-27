from turtle import Screen, Turtle
from typing import List, Tuple, Any

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('My snake Game')

starting_positions: List[Tuple] = [(0, 0), (-20, 0), (-40, 0)]
segments: list = []
game_on: bool = True

for position in starting_positions:
    snake_segment = Turtle('square')
    snake_segment.color('white')
    snake_segment.penup()
    snake_segment.goto(position)
    segments.append(snake_segment)


def snake_movement(segments):
    for seg in segments:
        seg.forward(20)

while game_on:
    snake_movement(segments)


screen.exitonclick()
