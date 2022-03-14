laptops = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30,
    "TOSHIBA": 10
}

brand = input("Input a brand: ")
amount = int(input("Input amount: "))
laptops[brand] = amount
laptops["DELL"] = 60
laptops["MACBOOK"] = 2

total = 0
for x in laptops:
    print("-", x, ":", laptops[x])
    total += laptops[x]

print("Total products:", total)
