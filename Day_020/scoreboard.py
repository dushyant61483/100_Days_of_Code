from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class GameScore(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,270)
    def show_score(self):
        self.color("white")
        self.hideturtle()
        self.clear()
        self.write(arg = f"Score: {self.score}",align=ALIGNMENT,font=FONT)
        self.score+=1

    def game_over(self):
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.write("Game Over",align=ALIGNMENT,font=FONT)
