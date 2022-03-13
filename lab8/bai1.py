def is_int(n):
    if n == int(n):
        return True
    else:
        return False


num = float(input("Input number: "))
if is_int(num):
    print(f'{int(num)} is an integer')
else:
    print(f'{num} is not an integer')