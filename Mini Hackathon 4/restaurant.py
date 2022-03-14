def get_order(m):
    current_order = {}
    while True:
        order = input("What would you like to order? ")
        current_order[order] = m[order]
        if complete():
            return current_order


def complete():
    choice = input("Anything else? y/n ")
    if choice == "n":
        return True
    else:
        return False


def output(list):
    print("Your order:")
    total = 0
    for x in list:
        print("-", x, ":", list[x])
        total += list[x]

    print("Total:", total)


menu = {
    "chicken": 20,
    "steak": 30,
    "rice": 5
}
output(get_order(menu))