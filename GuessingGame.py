# James Alan Bush
# CIS261002VA016-1236-001: Object-Oriented Computer Prog
# GuessingGame

import random

def display_heading():
    print("Guessing Game")
    
def play_game(limit):
    random_number = random.randint(1, 10)
    print(f"Guess a number between 1 and 10 in {limit} tries.")
    while limit != 0:
        guess = int(input(f"Enter your guess ({limit} tries remaining): "))
        limit = limit - 1;
        if guess < random_number:
            print(f"Too low! ({limit} tries remaining): ")
        elif guess > random_number:
            print(f"Too high! ({limit} tries remaining): ")
        else:
            print("Congratulations! You guessed the correct number!")
            break
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        main()
    else:
        print("Thanks for playing!")

def main():
    display_heading()
    limit = int(input("Enter the limit of attempts: "))
    play_game(limit)

main()