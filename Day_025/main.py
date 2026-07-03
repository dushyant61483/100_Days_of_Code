from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
screen.title("US States Guessing Game")
turtle = Turtle()
turtle.shape(image)
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < len(all_states):
    answer_text = screen.textinput(title= "Guess the state",prompt=f"Guess {len(guessed_states)+1}/{len(all_states)} state").title()
    if answer_text in all_states:
        if answer_text in guessed_states:
            continue
        else:
            guessed_states.append(answer_text)
            t = Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_text]
            t.goto(state_data.x.item(),state_data.y.item())
            t.write(answer_text)
    if answer_text == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        pd.DataFrame(missing_states).to_csv("missing_states.csv")
        break

screen.exitonclick()
