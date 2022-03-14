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

print("Total value of available brands:")
product = {}
total = 0
for x in quantity:
    product[x] = quantity[x] * laptops[x]
    print("-", x, ":", product[x])
    total += product[x]

print("Total products:", total)
