def is_prime(n):
    if n > 1:
        for j in range(2, int(n / 2) + 1):
            if (n % j) == 0:
                return False
                break
        return True
    else:
        return False


num = int(input("Input number: "))
print(f'First {num} prime(s):', end=" ")

count = 1
x = 2

while count <= num:
    if is_prime(x):
        print(x, end=" ")
        count += 1
        x += 1
    else:
        x += 1
