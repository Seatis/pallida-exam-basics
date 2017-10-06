import unittest
from unique_chars import *

class test_unique_chars(unittest.TestCase):

    def test_one_letter(self):
        self.assertEqual(unique_characters('a'), ['a'])
    
    def test_only_unique_letters(self):
        self.assertEqual(unique_characters('abc'), ['a', 'b', 'c'])

if __name__ == '__main__':
    unittest.main()