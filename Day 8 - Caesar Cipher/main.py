alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift *= -1
    
    for i in text:
        if i in alphabet:
            idx = alphabet.index(i)
            if (idx + shift) >= 26 or (idx + shift) < -26:
                end_text += alphabet[(idx+shift)%26]
            else:
                end_text += alphabet[(idx+shift)]
        else:
            end_text += i
    
    print(f"The {direction}d message is: {end_text}")  

def caesar_cipher():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    print("------------------------------------")

from art import logo
print(logo)

while True:
    caesar_cipher()
    choice = input("Do you want to restart the cipher program? Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if choice == "no":
        print("Goodbye.")
        break