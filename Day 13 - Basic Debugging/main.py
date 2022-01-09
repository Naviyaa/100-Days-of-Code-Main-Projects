############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# SOLUTION (set upper limit of range to 21)
print("Q1")
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()
print("-----------------\n")

#######################################################

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# SOLUTION (change randint range from 1-6 to 0-5)
print("Q2")
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
print("-----------------\n")

########################################################

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# SOLUTION (add >= in elif statement)
print("Q3")
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")
print("-----------------\n")

#######################################################

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# SOLUTION (add indentation for print, age is saved as int, add f for f-string)
print("Q4")
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
print("-----------------\n")

#######################################################

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# SOLUTION (remove == for word_per_page. Check values using print)
print("Q5")
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
#print(pages)
word_per_page = int(input("Number of words per page: "))
#print(word_per_page)
total_words = pages * word_per_page
print(total_words)
print("-----------------\n")

#######################################################

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

# SOLUTION (use debugger, choose a starting point and start)
# b_list.append wasn't under the for block, added it 
print("Q6")
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
print("-----------------\n")

#######################################################