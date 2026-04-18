from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
class Score(Turtle):
    def __init__(self,paddle):
        super().__init__()
        self.paddle = paddle
        self.score = -1
        self.color("white")
        self.penup()
        self.hideturtle()
        if self.paddle == 'right':
            self.goto(300, 250)
        else:
            self.goto(-300, 250)
        self.show_score()

    def show_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

