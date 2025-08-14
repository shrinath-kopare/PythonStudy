import random
from mimetypes import read_mime_types

import requests

response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
word = response.json()[0]
print(word)

# words = ["the", "are", "can"]
total_chances = 6
remaining_chances = total_chances


#generate random word
generated_word = word
# generated_word = "hooppy"

guessed_word = ["_"] * len(generated_word)

def guessed_word_string():
    print("".join(guessed_word))


print("Welcome to hangman game. You have 6 chances to guess.")

while remaining_chances > 0:
    print(f"-------Remaining chances : {remaining_chances}/{total_chances}")
    print("Guess the word: ", end="")
    guessed_word_string()

    guessed_letter = input("Enter the letter: ")
    if guessed_letter in generated_word:
        print("You guessed the word!")
        # index_of_letter = generated_word.index(guessed_letter)
        for i, letter in enumerate(generated_word):
            if letter == guessed_letter:
                guessed_word[i] = guessed_letter

    if "".join(guessed_word) == generated_word:
        print("You win!")
        break
    remaining_chances -= 1






