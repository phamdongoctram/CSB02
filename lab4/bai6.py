import turtle

t = turtle.Turtle()

n = int(input("Input number of edges: "))

for _ in range(n):
    turtle.forward(100)
    turtle.right(360 / n)

turtle.mainloop()