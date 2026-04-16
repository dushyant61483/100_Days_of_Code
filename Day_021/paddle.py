from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.x = pos[0]
        self.y = pos[1]
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.goto(self.x, self.y)

    def down(self):
        new_y = self.ycor()-40
        self.goto(self.xcor(), new_y)

    def up(self):
        new_y = self.ycor()+40
        self.goto(self.xcor(), new_y)


