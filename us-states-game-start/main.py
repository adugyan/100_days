from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)


answer_state = screen.textinput(title='Guess the State', prompt="What's another state's name?")
print(answer_state)