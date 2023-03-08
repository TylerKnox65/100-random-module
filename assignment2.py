#! python3

# SD Computing Studies Assignment
import random
choice = input("Choose Heads or Tails: ")
t = random.randint(1,2)
# Heads = 1, Tails = 2
if  "heads" in choice or "Heads" in choice: 
    if t == 1:
        print("You guessed right!")
    elif t == 2:
        print("You guessed wrong.")
if  "tails" in choice or "Tails" in choice: 
    if t == 2:
        print("You guessed right!")
    elif t == 1:
        print("You guessed wrong.")
