import unittest
from unique_chars import *

class test_unique_chars(unittest.TestCase):

    def test_one_letter(self):
        self.assertEqual(unique_characters('a'), ['a'])
    
    def test_only_unique_letters(self):
        self.assertEqual(unique_characters('abc'), ['a', 'b', 'c'])
    
    def test_anagram_word(self):
        self.assertEqual(unique_characters('anagram'), ['n', 'g', 'r', 'm'])
    
    def test_empty_string(self):
        self.assertEqual(unique_characters(''), 'No string given')
    
    def test_no_argument(self):
        self.assertEqual(unique_characters(), 'No string given')


if __name__ == '__main__':
    unittest.main()