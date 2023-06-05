import turtle

t = turtle.Pen()
t.speed(0)
t.penup()
turtle.bgcolor("black")

sides = int(turtle.numinput("Количество сторон", "Сколько сторон у вашей спирали из спиралей? (2-6) ", 4, 2, 6))
colors = ["red", "yellow", "blue", "green", "purple", "orange"]

for m in range(100):
    t.forward(m*15)
    position = t.position()
    heading = t.heading()
    print(position, heading)
    for n in range(int(m/2)):
        t.pendown()
        for x in range(5):
            t.circle(n * 4)
            t.left(360 / 5)
            t.pencolor(colors[x%5])
        t.penup()
    t.setx(position[0])
    t.sety(position[1])
    t.setheading(heading)
    t.left(360 / sides + 5)
turtle.done()
