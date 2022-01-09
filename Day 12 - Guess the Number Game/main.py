import random
from art import logo
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
#------------------------------------------------------

#Number of chances based on levels (global variables)
EASY_LEVEL = 10
HARD_LEVEL = 5

def choose_level():
    level = input("Choose difficulty level... Enter 'e' for easy and 'h' for hard: ")[0].lower()
    if level == 'e':
        return EASY_LEVEL
    elif level == 'h':
        return HARD_LEVEL

def check(guess_word, actual_word, turns):
    if guess_word > actual_word:
        print("Too high!")
        return turns - 1
    elif guess_word < actual_word:
        print("Too Low!")
        return turns - 1
    else:
        print(f"Yes!! {guess_word} is the correct number.")

def guess_game():
    print(logo)
    print("\nWelcome!\n")
    print("I am thinking of a number between 1 and 100...")

    num = random.randint(1, 100)

    turns = choose_level()
    guess = 0
    while guess != num:
        print(f"You have {turns} attempts left to make a guess.")
        guess = int(input("Guess a number: "))
        turns = check(guess, num, turns)
        if turns == 0:
            print("You have run out of turns...Game Over!")
            print(f"...The answer was {num}")
            break
        elif guess != num:
            print("Guess again!")

guess_game()