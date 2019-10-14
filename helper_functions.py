# Lab 01_01 Helper Functions
# Author: Chris Proctor and (Your Name)

from pathlib import Path
from random import choice

# This one is done for you. Check out the notes in the lab to understand this.
def get_words():
    """
    Reads the 10,000 most common English words from a file and returns them as a list.
    input: none
    output: a list of strings
    """
    filename = "10k_english_words.txt"
    return Path(filename).read_text().split()

# This one is also done for you.
def get_player_guess(choices):
    """
    Gets a guess from the player. If the guess isn't in choices, keeps asking the player
    for a guess until one is valid.
    input: list of strings
    output: str
    """
    guess = input("Guess a word: ")
    while guess not in choices:
        guess = input("Sorry, that's not a legal guess. Please try again: ")
    return guess

def has_five_letters(word):
    """
    Checks to see whether the word has five letters.
    input: str
    output: bool
    """
    pass # TODO

# You could check each letter against each other letter, but there's an easier way to do this.
# A set is like a list, but it never allows duplicates. If you try to add a second copy of an object 
# to a set, it's just ignored. So if you treat a string as a list of letters, and turn it into a set, 
# it will only contain distinct letters. Then you can compare the length of the set with the length 
# of the set. For example: 
#   >>> len("lemon")
#   5
#   >>> len(set("lemon"))
#   5
#   >>> len("apple")
#   5
#   >>> len(set("apple"))
#   4
def word_has_duplicate_letters(word):
    """
    Checks to see if a word has more than one of the same letter.
    For example, 'lemon' does not have duplicate letters but 'eagle' does.
    input: str
    output: bool
    """
    pass # TODO

# Before you do this part, read the sections of the Types lab titled "Using functions to transform and filter lists"
def get_five_letter_words_without_duplicate_letters(list_of_words):
    """
    Filters a list of words, returning just those which have five letters, and which contain
    no duplicate letters.
    input: a list of strings
    output: a list of strings
    """
    pass # TODO (You should write this function using a list comprehension)

# There are a few different ways to write this function; some are easier than others. It's a good idea
# to talk with your group about how you want to do it before diving in.
def count_common_letters(first_word, second_word):
    """
    Counts the number of letters shared by first_word and also in second_word. 
    inputs: two strings
    output: int
    """
    pass # TODO



