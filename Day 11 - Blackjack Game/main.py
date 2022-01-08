import random
from art import logo
from replit import clear

def deal_cards(cards):
    card = random.choice(cards)
    return card

def display(user_list, dealer_list):
    print("Your final hand:", user_list)
    print("Dealer's final hand:", dealer_list)

def calculate_score(cards_list):
    total = sum(cards_list)
    return total

def conditions(user, dealer, cards):
    if calculate_score(dealer) < 17:
        dealer.append(deal_cards(cards))

    if 11 in user and calculate_score(user) > 21:
        user[user.index(11)] = 1
    
    if 11 in dealer and calculate_score(dealer) > 21:
        dealer[dealer.index(11)] = 1


def compare_score(list1, list2):
    diff1 = 21 - calculate_score(list1)
    diff2 = 21 - calculate_score(list2)

    if diff1 < diff2:
        if diff1 >= 0:
            return 1
        else:
            return 0
    
    elif diff1 == diff2:
        return 2

    else:
        if diff2 >= 0:
            return 0
        else:
            return 1


def blackjack(user_cards, dealer_cards, cards):
    choice = input("Type 'y' to get another card, type 'n' to pass: ")[0].lower()
    conditions(user_cards, dealer_cards, cards)

    if choice == 'y':
        user_cards.append(deal_cards(cards))
        blackjack(user_cards, dealer_cards, cards)
    elif choice == "n":
        display(user_cards, dealer_cards)
        cmp = compare_score(user_cards, dealer_cards)
        if cmp == 0:
            print("Dealer wins!")
        elif cmp == 1:
            print("You win!")
        elif cmp == 2:
            print("It is a tie.")


while True:
    game = input("Do you want to play blackjack? Type 'y' for yes and 'n' for no.\n")[0].lower()
    if game == "y":
        clear()
        print(logo)
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        user_cards = []
        dealer_cards = []

        user_cards.append(deal_cards(cards))
        user_cards.append(deal_cards(cards))

        dealer_cards.append(deal_cards(cards))
        dealer_cards.append(deal_cards(cards))

        print("Your cards:", user_cards)
        print("One of Dealer's cards:", random.choice(dealer_cards))
        
        blackjack(user_cards, dealer_cards, cards)

    elif game == "n":
        clear()
        break