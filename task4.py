import random
    #roll 4 dice, discard the lowest b) roll 3 dice, reroll 1's.

print("Welcome to DnD dice roller")

choice = int(input("(Choose 1 for 'Roll 4 dice, discard lowest). Choose 2 for 'Roll 3 dice, reroll 1's. Or choose 3 to just roll 3 dice:  "))
if choice == 1:
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    d4 = random.randint(1,6)
    rlist = [d1, d2, d3, d4]
    dmin = min(rlist)
    rlist.remove(dmin)
    #rd = random.randint(1,6) // For adding back a random value.
    #rlist.append(rd)
    strength = sum(rlist)
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    d4 = random.randint(1,6)
    rlist = [d1, d2, d3, d4]
    dmin = min(rlist)
    rlist.remove(dmin)
    mind = sum(rlist)
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    d4 = random.randint(1,6)
    rlist = [d1, d2, d3, d4]
    dmin = min(rlist)
    rlist.remove(dmin)
    wisdom = sum(rlist)
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    d4 = random.randint(1,6)
    rlist = [d1, d2, d3, d4]
    dmin = min(rlist)
    rlist.remove(dmin)
    dex = sum(rlist)
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    d4 = random.randint(1,6)
    rlist = [d1, d2, d3, d4]
    dmin = min(rlist)
    rlist.remove(dmin)
    const = sum(rlist)
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    d4 = random.randint(1,6)
    rlist = [d1, d2, d3, d4]
    dmin = min(rlist)
    rlist.remove(dmin)
    chrsma = sum(rlist)
    print(f"Your strength is {strength}, Your int is {mind}, Your wisdom is {wisdom}, Your dexterity is {dex}, Your constitution is {const}, and your charisma is {chrsma}.")
    exit()

if choice == 2:
    d1 = random.randint(2,6)
    d2 = random.randint(2,6)
    d3 = random.randint(2,6)
    strength = d1 + d2 + d3
    d1 = random.randint(2,6)
    d2 = random.randint(2,6)
    d3 = random.randint(2,6)
    mind = d1 + d2 + d3
    d1 = random.randint(2,6)
    d2 = random.randint(2,6)
    d3 = random.randint(2,6)
    wisdom = d1 + d2 + d3
    d1 = random.randint(2,6)
    d2 = random.randint(2,6)
    d3 = random.randint(2,6)
    dex = d1 + d2 + d3
    d1 = random.randint(2,6)
    d2 = random.randint(2,6)
    d3 = random.randint(2,6)
    const = d1 + d2 + d3
    d1 = random.randint(2,6)
    d2 = random.randint(2,6)
    d3 = random.randint(2,6)
    chrsma = d1 + d2 + d3
    print(f"Your strength is {strength}, Your int is {mind}, Your wisdom is {wisdom}, Your dexterity is {dex}, Your constitution is {const}, and your charisma is {chrsma}.")
    exit()
elif choice == 3:
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    strength = d1 + d2 + d3
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    mind = d1 + d2 + d3
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    wisdom = d1 + d2 + d3
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    dex = d1 + d2 + d3
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    const = d1 + d2 + d3
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    chrsma = d1 + d2 + d3
    print(f"Your strength is {strength}, Your int is {mind}, Your wisdom is {wisdom}, Your dexterity is {dex}, Your constitution is {const}, and your charisma is {chrsma}.")
    exit()
else:
    print("Choose either 1, 2, or 3")
