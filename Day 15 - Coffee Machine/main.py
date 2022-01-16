MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0  # Amount of money earned by the machine


def check_resources(ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# Alt+shift and drag the cursor for multi-line editing
def get_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins...")
    q = int(input("Enter the number of quarters: "))
    d = int(input("Enter the number of dimes: "))
    n = int(input("Enter the number of nickles: "))
    p = int(input("Enter the number of pennies: "))
    total = (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)  # In dollars
    return total


def check_transaction(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    global money
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        money += drink_cost
        return True
    elif money_received == drink_cost:
        print("Amount entered is exact...$0 change.")
        money += drink_cost
        return True
    else:
        print("Sorry...you did not enter enough money. Money refunded.")
        return False


def make_coffee(drink_name, ingredients):
    """Deduct the required ingredients from the resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}.")


is_on = True

while is_on:
    print("---\nEnter 'off' to switch the machine off, or 'report' to get the list of resources and money earned.")
    choice = input("Enter a drink of your choice (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        print("Switching off...")
        is_on = False
    elif choice == "report":
        for k in resources:
            print(f"{k.capitalize()}: {resources[k]}")
        print(f"Money earned: ${money}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = get_coins()
            if check_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
