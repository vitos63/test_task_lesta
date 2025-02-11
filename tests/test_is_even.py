import unittest
from src.is_even_function import is_even

class TestIsEvenFunction(unittest.TestCase):
    def test_wrong_item(self):
        item = 'Some string'
        with self.assertRaises(ValueError):
            is_even(item)
    

    def test_even_items(self):
        for item in range(0,100,2):
            self.assertTrue(is_even(item))
    

    def test_odd_items(self):
        for item in range(1,100,2):
            self.assertFalse(is_even(item))

