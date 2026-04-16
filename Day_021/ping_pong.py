from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

l_paddle = Paddle((-380,0))
r_paddle = Paddle((380,0))
ball = Ball()
screen.listen()
screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")
screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")
is_game_on = True

while is_game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(r_paddle) < 20 and ball.xcor() > 350:
        print("why")
        ball.bounce_x()

screen.exitonclick()
