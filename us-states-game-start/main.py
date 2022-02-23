from turtle import Turtle, Screen
import pandas

screen = Screen()
turtle = Turtle()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data['state'].to_list()
guessed_states = []


def place_name():
    t = Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data['state'] == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.pendown()
    t.write(answer_state)


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}",
                                    prompt="What's another state's name?").title()
    guessed_states.append(answer_state)
    if answer_state in all_states:
        place_name()
    elif 'Exit' in guessed_states:
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('state_to_learn')



