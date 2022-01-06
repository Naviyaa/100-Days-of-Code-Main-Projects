#1. Create a greeting for your program.
print("Welcome to Band Name Generator!\n")

#2. Ask the user for the city that they grew up in.
city = input("Which city did you grow up in?\n")

#3. Ask the user for the name of a pet.
pet = input("What's the name of your pet?\n")

#4. Combine the name of their city and pet and show them their band name.
band_name = city.title() + " " + pet.title()

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end
print("Your band name could be: " + band_name)