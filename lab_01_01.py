# Lab 01_01
# Author: Chris Proctor and (Your Name)
# -------------------------------------
# Plays the word game Jotto.

from helper_functions import *

def jotto_game():
    all_words = get_words()
    legal_words = get_five_letter_words_without_duplicate_letters(all_words)
    secret_word = choice(legal_words)
    # print(secret_word) # Uncomment this line if you want to cheat!
    print("Welcome to Jotto. See if you can guess the secret word.")
    guess = get_player_guess(legal_words)
    while guess != secret_word:
        num_letters_right = count_common_letters(guess, secret_word)
        print("It's not the secret word, but your guess has {} letters correct.".format(num_letters_right))
        guess = get_player_guess(legal_words)
    print("You got it!")
        
if __name__ == '__main__': 
    jotto_game()
