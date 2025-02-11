import unittest
from random import randint
from src.sorting_algorithm import merge_sort

class TestMergeSort(unittest.TestCase):
    def test_sorted_numbers(self):
        numbers = list(range(-100, 100))
        sorted_numbers = merge_sort(numbers)

        self.assertEqual(sorted_numbers, numbers)
    

    def test_reverse_sorted_numbers(self):
        numbers = list(range(-100, 100))[::-1]
        sorted_numbers = merge_sort(numbers)

        self.assertEqual(sorted_numbers, sorted(numbers))
    

    def test_reverse_random_numbers(self):
        numbers = [randint(-100,100) for _ in range(300)]
        sorted_numbers = merge_sort(numbers)

        self.assertEqual(sorted_numbers, sorted(numbers))