import turtle
t = turtle.Turtle()

# drawing first side
t.forward(100)
t.left(90)

# drawing second side
t.forward(80)
t.left(90)

# drawing third side
t.forward(100)
t.left(90)

# drawing fourth side
t.forward(80)
t.left(180)

t.pencolor('#de5246')
t.width(5)
t.penup()
t.goto(100, 0)
t.pendown()
t.forward(82)
t.left(135)
t.forward(70.7)
t.right(90)
t.forward(70.7)
t.left(135)
t.forward(82)
turtle.done()