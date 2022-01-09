# Generate a random account from the game data.
# Format account data into printable format.
# Ask user for a guess.
# Check if user is correct.
## Get follower count.
## If Statement
# Feedback.
# Score Keeping.
# Make game repeatable.
# Make B become the next A.
# Add art.
# Clear screen between rounds.

###############################################

from replit import clear

import random
from art import logo, vs
from game_data import data

def get_acc():
  return random.choice(data)

def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess, followers1, followers2):
  if followers1 > followers2:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  account_a = get_acc()
  account_b = get_acc()

  while True:
    account_a = account_b
    account_b = get_acc()

    while account_a == account_b:
      account_b = get_acc()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      break

game()