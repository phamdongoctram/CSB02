num = int(input("Input a number: "))
count = 0
while num != 0:
    num //= 10
    count += 1

print("This number has", count, "digit(s).")