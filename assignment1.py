import random

number = random.randint(1, 100)


num_guesses = 0

while True:
    guess = int(input("Guess the number between 1 and 100: "))
    num_guesses = num_guesses + 1
    
    if guess < number:
        print("Too low. Try again.")
    elif guess > number:
        print("Too high. Try again.")
    else:
        print(f"Congratulations! You guessed the number in " + str(num_guesses) + " guesses.")
        exit()
