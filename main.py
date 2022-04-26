import turtle
import pandas
from state import State
#
# FONT = ("Courier", 10, "normal")
#
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()
turtle.shape(image)
score = 0

state = State()

game_is_on = True
while game_is_on :

    answer_state = screen.textinput(title = "Guess the country", prompt= "What's another state's name?")
    if score == 50 or answer_state == "quit":
        quit()
    answer_state = answer_state.title()

    if answer_state in states:
        coordinates = data[data.state == answer_state]
        x_coordinate = int(coordinates.x)
        y_coordinate = int(coordinates.y)
        state_coordinates = (x_coordinate,y_coordinate)
    else:
        continue
    state.create_state(state_coordinates,answer_state)

    score += 1


screen.exitonclick()
