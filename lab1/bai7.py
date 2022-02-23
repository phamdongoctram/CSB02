import turtle

t = turtle.Turtle()
length = 200
angle = 90
x = -length // 2
y = -length // 2

t.penup()
t.goto(x, y)
t.pendown()
for i in range(4):
    t.forward(200)
    t.left(90)

angle = angle - 45
x = x + 100
y = y - 30
t.penup()
t.goto(x, y)
t.pendown()
t.left(45)
for i in range(4):
    t.forward(200)
    t.left(90)

turtle.done()
