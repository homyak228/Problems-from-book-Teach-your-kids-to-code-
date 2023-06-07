import turtle

print("SpirralMyName.py")

t = turtle.Pen()
turtle.bgcolor("black")
name = turtle.textinput("Ввод данных", "Назовите всех членов своей семьи. Если их больше нет, введите \"q\"")
names = []

while name != "q":
    name = turtle.textinput("Ввод данных", "Назовите всех членов своей семьи. Если их больше нет, введите \"q\"")
    if name != "q":
        names.append(name)

colors = ["red", "yellow", "blue", "lime"]

for x in range(100):
    t.pencolor(colors[x%len(names)])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(names[x%len(names)], font = ("Arial", int((x + 4)/4), "bold"))
    t.left(92)
