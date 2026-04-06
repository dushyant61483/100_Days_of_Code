from turtle import Turtle,Screen
import random



is_racing = False
screen = Screen()
screen.setup(width=800,height=600)
user_bet = screen.textinput(title="Welcome to Turtle Racing Game",prompt="Select the color of Turtle going to win!!").lower()
colors = ["red","orange","yellow","green","blue","violet"]
y = [-200,-120,-40,40,120,200]
turtle_lists = []

def move():
    steps = random.randint(0,5)
    return steps


for i in range(6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-380, y[i])
    turtle_lists.append(new_turtle)

if user_bet:
    is_racing = True

while is_racing:

    for turt in turtle_lists:
        turt.forward(move())
        if turt.position()[0] > 380:
            is_racing = False
            win_turtle = turt.pencolor()
            if win_turtle == user_bet:
                print("You win!")
            else:
                print("You lose! Wining turtle is", win_turtle)
screen.title("Game Over")
