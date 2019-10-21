# Test helper functions for lab 01 01
# Author: Chris Proctor
# ------------------------------------
# These automated tests will tell you whether your helper functions are working correctly. 
# Once they are working, you should be able to run lab_01_01 to play the game Jotto!

import unittest
from helper_functions import *

class TestHelperFunctions(unittest.TestCase):

    def test_has_five_letters(self):
        self.assertTrue(has_five_letters("lemon"))
        self.assertTrue(has_five_letters("eagle"))
        self.assertFalse(has_five_letters("eagles"))
        self.assertFalse(has_five_letters(""))

    def test_word_has_duplicate_letters(self):
        self.assertTrue(word_has_duplicate_letters("apple"))
        self.assertTrue(word_has_duplicate_letters("eagle"))
        self.assertFalse(word_has_duplicate_letters("lemon"))
        self.assertFalse(word_has_duplicate_letters("number"))

    def test_get_five_letter_words_without_duplicate_letters(self):
        word_list = ["a", "eagle", "lemon", "eagles", "number"]
        result = get_five_letter_words_without_duplicate_letters(word_list)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "lemon")

    def test_count_common_letters(self):
        self.assertEqual(count_common_letters("lemon", "melon"), 5)
        self.assertEqual(count_common_letters("mouse", "melon"), 3)
        self.assertEqual(count_common_letters("mouse", "trick"), 0)

