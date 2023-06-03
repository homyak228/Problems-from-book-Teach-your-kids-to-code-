import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")

colors = ["red", "orange", "yellow", "lime", "green", "light blue", "blue", "purple"]
sides = int(turtle.numinput("Сколько сторон?", "Сколько сторон вы хотите нарисовать? (1-8)", 4, 1, 8))

for x in range(360):
    t.pencolor(colors[x % sides])
    t.circle(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
