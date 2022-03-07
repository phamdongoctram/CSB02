num = int(input("Input number: "))
sum = 0
n = num
while n != 0:
    sum = sum + (n % 10)
    n = n // 10
print("Sum of digits of", num, "=", sum)

