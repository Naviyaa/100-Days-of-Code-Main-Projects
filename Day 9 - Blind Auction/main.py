from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

print("Welcome to the Secret Auction Program.")

auction = []

while True:
    bidding = {}
    name = input("What is your name?\n")
    bid = float(input("What is your bid amount (in $)?\n"))

    bidding["name"] = name
    bidding["bid_amount"] = bid

    auction.append(bidding)

    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if choice == "no":
        break
    elif choice == "yes":
        clear()
        continue

winner = {"name": "", "max_bid": -1}

for bids in auction:
    if bids["bid_amount"] > winner["max_bid"]:
        winner["max_bid"] = bids["bid_amount"]
        winner["name"] = bids["name"]

print(f"The winner is {winner['name']} with a bid of ${winner['max_bid']}")