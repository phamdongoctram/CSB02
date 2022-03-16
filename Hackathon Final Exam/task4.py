is_complete = True
order_list = []
print("== Welcome to MindX Restaurant ==")

while is_complete:
    print()
    d = input("Please choose a dish: ")
    if d in order_list:
        yn = input("You chose this already. Anything else? (y/n): ")
    else:
        order_list.append(d)
        yn = input("Great choice! Anything else? (y/n): ")
    if yn == "y":
        is_complete = True
    else:
        is_complete = False

print()
print("Well done! Your order: ")
for i in order_list:
    print("- ", i)