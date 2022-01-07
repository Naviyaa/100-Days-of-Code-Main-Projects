from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

print("Welcome to the Secret Auction Program.")

bidding = {}

while True:    
    name = input("What is your name?\n")
    bid = float(input("What is your bid amount (in $)?\n"))
    bidding[name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if choice == "no":
        clear()
        break
    elif choice == "yes":
        clear()

name=""
winner = {name: -1}

for bidder in bidding:
    if bidding[bidder] > winner[name]:
        name = bidder
        winner[name] = bidding[bidder]

print(f"The winner is {name} with a bid of ${winner[name]}")