from replit import clear
from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(logo)

def calculator():
    num1 = float(input("Enter the first number: "))

    for symbol in operations:
        print(symbol)

    while True:    
        opr = input("Choose a valid operation: ")
        if opr not in operations:
            print(f"{opr} is not a valid operation symbol.")
            while opr not in operations:
                opr = input("Choose a valid operation: ")

        num2 = float(input("Enter the next number: "))

        calc_func = operations[opr]
        ans = calc_func(n1 = num1, n2 = num2)

        print(f"The solution for {num1} {opr} {num2} is: {ans}")
        print("----------------******-----------------")

        choice = input(f"Enter 'yes' to continue with another operation on {ans}? Enter 'no' to execute operations with new values. Enter 'exit' to stop/exit the program.\n").lower()

        if choice == "exit":
            clear()
            print("Goodbye.")
            break
            
        elif choice == "yes":
            num1 = ans
            clear()
        
        elif choice == "no":
            clear()
            calculator()
            break

calculator()