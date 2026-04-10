from turtle import Turtle
STARTING_COORDINATES = [(0,0) , (-20,0),(-40,0)]
MOVING_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.origin = 0
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_COORDINATES:
            if pos == (0,0):
                self.add_snake(pos,"red")
            else:
                self.add_snake(pos)

    def add_snake(self,position,color="white"):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color(color)
        new_segment.speed("fastest")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_snake(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVING_SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

