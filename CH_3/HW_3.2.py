import turtle

print("SpirralMyName.py")

t = turtle.Pen()
turtle.bgcolor("black")

your_name = turtle.textinput("Ввод данных", "Как тебя зовут?")
sides = int(turtle.numinput("Сколько сторон?", "Сколько сторон вы хотите рарисовать? (1-4)", 2, 1, 4))

colors = ["red", "yellow", "blue", "lime"]

for x in range(100):
    t.pencolor(colors[x%sides])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(your_name, font = ("Arial", int((x + 4)/4), "bold"))
    t.left(360 / sides + 2)
