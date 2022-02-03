from turtle import Turtle

P1_POSITION: dict = {'x_pos': -350, 'y_pos': 0}
P2_POSITION: dict = {'x_pos': 350, 'y_pos': 0}
DIRECTIONS: dict = {'Up': 90, 'Down': 270}

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)


    def move_up(self):
        new_y = self.paddle() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.paddle() + 20
        self.goto(self.xcor(), new_y)

            
    