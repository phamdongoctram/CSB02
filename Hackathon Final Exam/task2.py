import math

a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

discriminant = b**2 - 4 * a * c
sqrt_dis = math.sqrt(abs(discriminant))

if discriminant > 0:
    print("The equation has 2 solutions.")
    print(f'x = {(-b + sqrt_dis) / (2 * a)} or x = {(-b - sqrt_dis) / (2 * a)}')
elif discriminant == 0:
    print(f'x = {-b / (2 * a)}')
else:
    print("The equation doesn't have any real roots.")
