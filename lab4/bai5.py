def check(n):
    sum = 0
    while n != 0:
        sum = sum + (n % 10)
        n = n // 10
    if sum == 9:
        return True
    else:
        return False


out = [0] * 10
x = 1008
i = 0
while out[9] == 0:
    if check(x):
        out[i] = x
        x = x + 1
        i = i + 1
    else:
        x = x + 1
        check(x)
print(out)
