import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choices = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user >=3 or user < 0:
  print("Invalid choice. You can only choose 0, 1 or 2.")
else:
  print("User chose:")
  print(choices[user])
  
  computer = random.randint(0, len(choices) - 1)
  print("Computer chose:")
  print(choices[computer])

  if (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
    print("You win")
  elif user == computer:
    print("It is a tie.")
  else:
    print("You lose")