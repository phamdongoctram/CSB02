num = int(input("Input number: "))
factorial = 1
if num < 0:
    print("Invalid")
elif num == 0:
    print("0! = 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(str(num) + "! =", factorial)