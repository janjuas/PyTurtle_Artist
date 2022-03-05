import turtle
from turtle import *
import random
import colorgram

screen = Screen()
height = 550
width = 550
screen.setup(width,height)

damien = Turtle()

damien.speed(0)
colours = colorgram.extract('image.jpeg', 10)

colour_palette = []
for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    colour_palette.append((r, g, b))

x_pos = -200
y_pos = -200
damien.hideturtle()
damien.pu()
damien.setposition(x_pos, y_pos)
turtle.colormode(255)
dot_count = 100
while dot_count != 0:
    x = 0
    y = 0
    while y != 10:
        while x != 10:
            damien.dot(20, random.choice(colour_palette))
            damien.pu()
            damien.fd(50)
            damien.pd()
            x += 1
            dot_count -= 1
        y += 1
        y_pos += 5
        damien.pu()
        damien.setposition(x_pos, y_pos)
        damien.pd()





screen.exitonclick()
