import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
turtle = Player()
game_is_on = True
screen.listen()
screen.onkey(turtle.move, "Up")
level = Scoreboard()

cars = CarManager()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    if turtle.ycor() > 280:
        turtle.reset_position()
        level.update()
        cars.move_increment()

    for car in cars.all_cars:
            if car.distance(turtle) < 20:
                game_is_on = False
                level.game_over()
screen.exitonclick()

