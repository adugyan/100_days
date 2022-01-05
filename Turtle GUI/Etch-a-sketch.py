from turtle import Screen, Turtle

timmy = Turtle()
screen = Screen()


def move_forward() -> None:
    timmy.forward(10)


def move_backwards() -> None:
    timmy.backward(10)


def clockwise():
    current_setting = timmy.heading()
    timmy.setheading(current_setting - 10)


def counterclockwise() -> None:
    current_setting = timmy.heading()
    timmy.setheading(current_setting + 10)


def clear() -> None:
    timmy.clear()
    timmy.reset()


screen.onkey(fun=clear, key='c')
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backwards, key='s')
screen.onkey(fun=clockwise, key='d')
screen.onkey(fun=counterclockwise, key='a')
screen.listen()
screen.exitonclick()
