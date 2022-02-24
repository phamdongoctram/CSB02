num = int(input("Input number: "))
x = 0
if num % 3 == 0:
    if num % 5 == 0:
        print(num, "is divisible by 3 and 5")
    else:
        print(num, "is divisible by 3")
elif num % 5 == 0:
    print(num, "is divisible by 5")
else:
    print(num, "is not divisible by 3 or 5")