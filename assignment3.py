#! Python3
import random

choice = str(input("Enter Rock, Paper, or Scissors: "))
comp = random.randint(1,3)

#For comp, 1 = Rock, 2 = Paper, 3 = Scissors
if "Rock" in choice or "rock" in choice:
    if comp == 1:
        print("Tie")
    elif comp == 2:
        print("You lose. The computer chose Paper.")
    elif comp == 3:
        print("You win! The computer chose Scissors!")
elif "Paper" in choice or "paper" in choice:
    if comp == 2:
        print("Tie")
    elif comp == 3:
        print("You lose. The computer chose Scissors.")
    elif comp == 1:
        print("You win! The computer chose Rock!")
elif "Scissors" in choice or "scissors" in choice:
    if comp == 3:
        print("Tie")
    elif comp == 1:
        print("You lose. The computer chose Rock.")
    elif comp == 2:
        print("You win! The computer chose Paper!")
