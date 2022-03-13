def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    return fact


num = int(input("Input number: "))
result = 0
for i in range(1, num + 1):
    result += factorial(i) / i

print("Result:", int(result))