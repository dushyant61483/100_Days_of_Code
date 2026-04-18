from turtle import Screen
from paddle import Paddle
from ball import Ball
from leaderboard import Score
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

l_paddle = Paddle((-380,0))
r_paddle = Paddle((380,0))
ball = Ball()
score_left = Score("right")
score_right = Score("left")
screen.listen()
screen.listen()
screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")
screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")
is_game_on = True

sleep_time = 0.07
while is_game_on:
    time.sleep(sleep_time)
    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 350:
        ball.bounce_x()
        sleep_time *= 0.92

    if ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()
        sleep_time *= 0.92

    if  ball.xcor() < -430 :
        ball.reset_position()
        score_left.show_score()
        sleep_time = 0.1

    if ball.xcor() > 430:
        ball.reset_position()
        score_right.show_score()
        sleep_time = 0.1
screen.exitonclick()
