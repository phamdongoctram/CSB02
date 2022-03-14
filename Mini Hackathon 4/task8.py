import random

skills = [
    {"Skill 1": {
        "Name": "Tackle",
        "Minimum level": 1,
        "Damage": 5,
        "Hit rate": 0.3
    }},
    {"Skill 2": {
        "Name": "Quick Attack",
        "Minimum level": 2,
        "Damage": 3,
        "Hit rate": 0.5
    }},
    {"Skill 3": {
        "Name": "Strong Kick",
        "Minimum level": 3,
        "Damage": 9,
        "Hit rate": 0.2
    }}
]

print("Skill 1:", skills[0]["Skill 1"]["Name"])
print("Skill 2:", skills[1]["Skill 2"]["Name"])
print("Skill 3:", skills[2]["Skill 3"]["Name"])
skill = int(input("Choose skill by number: "))
if skill == 1:
    print("You chose", skills[0]["Skill 1"]["Name"])
    hit_rate = skills[0]["Skill 1"]["Hit rate"]
    damage = skills[0]["Skill 1"]["Damage"]
elif skill == 2:
    print("You chose", skills[1]["Skill 2"]["Name"])
    hit_rate = skills[1]["Skill 2"]["Hit rate"]
    damage = skills[1]["Skill 2"]["Damage"]
else:
    print("You chose", skills[2]["Skill 3"]["Name"])
    hit_rate = skills[2]["Skill 3"]["Hit rate"]
    damage = skills[2]["Skill 3"]["Damage"]

if random.random() < hit_rate:
    print("Damage:", damage)
else:
    print("Missed.")
    