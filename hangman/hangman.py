import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

word_to_guess = get_valid_word(words)
word_to_guess_letters = set(word_to_guess)
used_letters = set()
alphabet = set(string.ascii_uppercase) #alphabet letters

lives = len(word_to_guess_letters)

while len(word_to_guess_letters) > 0 and lives>0:
    print(f"You have {lives} remaining lives.\nYou used this letters: {' '.join(used_letters)}.")
    word_list = [letter if letter in used_letters else '-' for letter in word_to_guess]
    print(f"The word you need to guess: {' '.join(word_list)}")
    user_input = input("Pick a letter: ").upper()

    if user_input in alphabet-used_letters:
        used_letters.add(user_input)
        if user_input in word_to_guess_letters:
            word_to_guess_letters.remove(user_input)
        else:
            lives-=1
            print(f"\n{user_input} is not in the word.") 
    elif user_input in used_letters:
        print(f"Letter {user_input} is already used, please try again.")
    else:
        print(f"\n{user_input} is an invalid charcter, please enter a valid character.")
    
if lives==0:
    print(f"You died, the word was {word_to_guess}")
else:
    print(f"Congrats you won, the word is {word_to_guess}")
    
