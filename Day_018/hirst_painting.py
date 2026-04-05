# import colorgram as col
# colors = col.extract("hirst painting.jpg",10)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r,g,b)
#     rgb_colors.append(rgb)
import turtle
import random
color_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162)]

timmy = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
timmy.pensize(10)
timmy.speed("fastest")
timmy.hideturtle()
# turtle.bgcolor(0,0,0)
def moving(parts):
    for _ in range(10):
        timmy.dot(random.choice(color_list))
        timmy.penup()
        timmy.forward(parts)
        timmy.pendown()

def position(pos,parts):
    y = 0
    while timmy.pos() != (pos,pos):
        moving(parts)
        y += parts
        timmy.teleport(0,y)


position(timmy.pos(),50)
screen.exitonclick()
