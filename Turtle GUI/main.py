import turtle
from turtle import Turtle, Screen
from random import choice, randint


"""
There can be a menu for the shapes. Dictionary with each shape having a number of sides key.
User choices will be appended into a list
A static method will look at the above list of dictionaries get the associated number of sides value and then
use the as input for the for loop and divide no of sides by 360 as input for the angle
"""

timmy = Turtle()
timmy.shape("turtle")
turtle.colormode(255)
timmy.speed('fastest')


def draw_shapes(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


def dashed_line():
    for _ in range(4):
        timmy.forward(25)
        timmy.penup()
        timmy.forward(12.5)
        timmy.pendown()


def random_walk():
    timmy.pensize(15)
    turn_angles = [0, 90, 180, 270]
    timmy.forward(50)
    timmy.setheading(choice(turn_angles))


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    colors: tuple = (r, g, b)
    return colors


def triangle_decagon():
    for _ in range(3, 11):
        random_colors = random_color()
        timmy.color(random_colors)
        draw_shapes(_)


for _ in range(200):
    random_colors = random_color()
    timmy.color(random_colors)
    random_walk()

screen = Screen()
screen.exitonclick()
