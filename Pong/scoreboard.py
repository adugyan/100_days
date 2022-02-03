from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.p1_score = 0
        self.p2_score = 0
        self.create_p1_scoreboard()
        self.create_p2_scoreboard()
        self.hideturtle()

    def create_p1_scoreboard(self):
        self.penup()
        self.goto(-100, 270)
        self.write(f"{self.p1_score}", align="center", font=("Courier", 20, "normal"))

    def create_p2_scoreboard(self):
        self.penup()
        self.goto(100, 270)
        self.write(f"{self.p2_score}", align="center", font=("Courier", 20, "normal"))
