def is_prime(n):
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                return False
                break
        return True
    else:
        return False


num = int(input("Input number: "))
if is_prime(num):
    print(f'{num} is a prime')
else:
    print(f'{num} is not a prime')