#HW_2.1.py -> Modiffed: SuperColorSpirral.py

import turtle

turtle.bgcolor("black")
t = turtle.Pen()
t.speed(0)
sides = 3
colors = ["red", "yellow", "blue", "orange", "green", "purple"]

for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x *3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)
