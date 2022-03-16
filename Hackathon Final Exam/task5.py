phones = {
    "Iphone 12": 28000000,
    "Samsung N10": 16000000,
    "Oppo 93": 7500000,
    "Vsmart": 7400000,
    "Vivo": 4200000
}

# 1
name = input("Input name of a phone: ")
print("Price of", name, ":", phones[name])

# 2
budget = int(input("Input your budget: "))
print("Phones that fit your budget:")
for x in phones:
    if phones[x] <= budget:
        print("-", x, ":", phones[x])
    else:
        continue
