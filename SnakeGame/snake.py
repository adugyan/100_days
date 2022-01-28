from turtle import Turtle
from typing import List, Tuple

MOVE_DISTANCE: int = 20
STARTING_POSITIONS: List[Tuple] = [(0, 0), (-20, 0), (-40, 0)]
DIRECTIONS: dict = {'Right': 0, 'Up': 90, 'Left': 180, 'Down': 270}


class Snake:
    def __init__(self):
        self.segments: list = []
        for position in STARTING_POSITIONS:
            snake_segment = Turtle('square')
            snake_segment.color('white')
            snake_segment.penup()
            snake_segment.goto(position)
            self.segments.append(snake_segment)
            
        self.head = self.segments[0]

    def move(self):
        # Reminder the variable integer becomes the [index_key] when range is in play
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_left(self):
        if self.head.heading() != DIRECTIONS['Right']:
            self.head.setheading(DIRECTIONS['Left'])

    def move_right(self):
        if self.head.heading() != DIRECTIONS['Left']:
            self.head.setheading(DIRECTIONS['Right'])

    def move_up(self):
        if self.head.heading() != DIRECTIONS['Down']:
            self.head.setheading(DIRECTIONS['Up'])

    def move_down(self):
        if self.head.heading() != DIRECTIONS['Up']:
            self.head.setheading(DIRECTIONS['Down'])
