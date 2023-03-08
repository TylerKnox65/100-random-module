import random
    #roll 4 dice, discard the lowest b) roll 3 dice, reroll 1's.

print("Welcome to DnD dice roller")
choice = int(input("(Choose 1 for 'Roll 4 dice, discard lowest)-Dont pick. Choose 2 for 'Roll 3 dice, reroll 1's. Or choose 3 to just roll 3 dice:  "))
"""
if choice == 1:
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    d4 = random.randint(1,6)
    min = min(d1, d2, d3 , d4)
    if d1 == min:
        strength = d2 + d3 + d4
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        d3 = random.randint(1,6)
        d4 = random.randint(1,6)
        min = min(d1, d2, d3 , d4)
        if d1 == min:
            wisdom = d2 + d3 + d4
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            d3 = random.randint(1,6)
            d4 = random.randint(1,6)
            min = min(d1, d2, d3 , d4)
            if d1 == min:
                mind = d2 + d3 + d4
                d1 = random.randint(1,6)
                d2 = random.randint(1,6)
                d3 = random.randint(1,6)
                d4 = random.randint(1,6)
                min = min(d1, d2, d3 , d4)
                if d1 == min:
                    dex = d2 + d3 + d4
                    d1 = random.randint(1,6)
                    d2 = random.randint(1,6)
                    d3 = random.randint(1,6)
                    d4 = random.randint(1,6)
                    min = min(d1, d2, d3 , d4)
                    if d1 == min:
                        const = d2 + d3 + d4
                        d1 = random.randint(1,6)
                        d2 = random.randint(1,6)
                        d3 = random.randint(1,6)
                        d4 = random.randint(1,6)
                        min = min(d1, d2, d3 , d4)
                        if d1 == min:
                            chrsma = d2 + d3 + d4




    elif d2 == min:
        print("")
    elif d3 == min:
        print("")
    elif d4 == min:
        print("")
"""#Takes too long, not doing it.
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
    
else:
    print("Choose either 1, 2, or 3")
