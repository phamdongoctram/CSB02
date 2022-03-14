laptops = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400
}
quantity = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}

# 1
print("Total price:", laptops["ASUS"]*5)

# 2, 3
brand = input("Input a brand: ")
amount = int(input("Input amount to buy: "))
print("Total price:", laptops[brand]*amount)

print("Available products:")
quantity[brand] -= amount
for x in quantity:
    print("-", x, ":", quantity[x])