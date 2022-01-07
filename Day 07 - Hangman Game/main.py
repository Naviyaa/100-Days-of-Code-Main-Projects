#Hangman Game
import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo, stages
print(logo)

display = []
for _ in range(word_length):
    display += "_"

guessed_words = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess not in guessed_words:
        guessed_words.append(guess)
    else:
        print(f"The letter '{guess}' has already been guessed.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"Letter '{guess}' is not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])

if lives == 0:
    print("The word is: " + chosen_word)