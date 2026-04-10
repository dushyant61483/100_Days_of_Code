from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import GameScore
screen = Screen()
screen.tracer(0)

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()
score = GameScore()
game_is_on = True
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

score.show_score()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score.show_score()
    if snake.head.xcor()> 280 or snake.head.xcor()<-280 or snake.head.ycor()> 280 or snake.head.ycor()<-280:
        game_is_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()

