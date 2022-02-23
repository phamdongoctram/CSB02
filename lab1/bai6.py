import turtle

t = turtle.Turtle()
length = 200
angle = 90
width = 8


def draw_square(t, x, y, length, width, angle):
    t.width(width)
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(4):
        t.forward(length)
        t.left(angle)


for i in range(2):
    startx = -length // 2
    starty = -length // 2
    length = length - 30
    width = width - 2
    startx = -length // 2
    starty = -length // 2
    draw_square(t, startx, starty, length, width, angle)

turtle.done()