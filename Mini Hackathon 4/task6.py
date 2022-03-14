# 1
character = {"Name": "Light", "Age": 17, "Strength": 8, "Defense": 10, "HP": 100, "Backpack": ["Shield", "Bread Loaf"],
             "Gold": 100, "Level": 2}
# 2
character["Gold"] += 50
print("Gold:", character["Gold"])
# 3
character["Backpack"].append("FlintStone")
print("Backpack:", end=" ")
for i in character["Backpack"]:
    print(i, end=", ")