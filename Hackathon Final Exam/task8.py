n = int(input("Input a number: "))
print("First", n, "Fibonacci numbers:", end=" ")
f1 = 0
f2 = 1
if n < 1:
    print(f1, end=" ")
for x in range(1, n+1):
    print(f2, end=" ")
    next_number = f1 + f2
    f1 = f2
    f2 = next_number

