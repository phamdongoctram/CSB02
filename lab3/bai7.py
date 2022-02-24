import turtle

l1 = float(input("Input length 1: "))
l2 = float(input("Input length 2: "))
l3 = float(input("Input length 3: "))


def check_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False


def check_right_triangle(a, b, c):
    if b**2 + c**2 == a**2:
        return True
    elif a**2 + c**2 == b**2:
        return True
    elif a**2 + b**2 == c**2:
        return True
    else:
        return False


def check_equilateral_triangle(a, b, c):
    if a == b == c:
        return True
    else:
        return False


def draw(x):
    board = turtle.Turtle()

    board.forward(x)

    board.left(120)
    board.forward(x)

    board.left(120)
    board.forward(x)

    turtle.done()


if check_triangle(l1, l2, l3):
    if check_right_triangle(l1, l2, l3):
        print("The 3 line segments can form a right triangle.")
    elif check_equilateral_triangle(l1, l2, l3):
        print("The 3 line segments can form an equilateral triangle.")
        draw(l1)
    else:
        print("The 3 line segments can form a triangle.")
else:
    print("The 3 line segments cannot form a triangle.")