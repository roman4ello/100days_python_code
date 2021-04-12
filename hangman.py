import os
import random

from hangman_art import logo, stages
from hangman_words import word_list


def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

display = []
for i in range(word_length):
    display += "_"

endOfTheGame = False

print(logo)
while not endOfTheGame:
    guess = input("Guess a letter: ").lower()
    # os.system('clear')
    clear()
    if guess in display:
        print(f'You already chose: {guess}. ')

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")

    if "_" not in display:
        endOfTheGame = True
        print("You win.")

    if guess not in chosen_word:
        print(f'Letter >> {guess} <<  not in the word. ')
        lives -= 1
        if lives == 0:
            print("You lose.")
            endOfTheGame = True

    print(stages[lives])
