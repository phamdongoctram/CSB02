l1 = float(input("Input length 1: "))
l2 = float(input("Input length 2: "))
l3 = float(input("Input length 3: "))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print("The 3 line segments can form a triangle.")
else:
    print("The 3 line segments cannot form a triangle.")

