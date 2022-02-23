deposit = float(input("Deposit: "))


def account(d, y):
    return d * 1.05 ** y


print("Account after 1 year:", account(deposit, 1))
print("Account after 2 years:", account(deposit, 2))
print("Account after 10 years:", account(deposit, 10))
