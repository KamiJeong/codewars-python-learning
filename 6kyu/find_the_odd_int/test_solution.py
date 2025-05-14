import unittest
from solution import find_it

class TestFindIt(unittest.TestCase):
    def test_single_odd_occurrence(self):
        self.assertEqual(find_it([7]), 7)

    def test_multiple_numbers(self):
        self.assertEqual(find_it([1, 1, 2, 2, 3]), 3)

    def test_large_sequence(self):
        self.assertEqual(find_it([10, 10, 10, 20, 20, 10]), None)

    def test_negative_numbers(self):
        self.assertEqual(find_it([-1, -1, -2, -2, -3, -3, -3]), -3)

    def test_no_odd_occurrence(self):
        self.assertEqual(find_it([2, 2, 4, 4]), None)

    def test_mixed_numbers(self):
        self.assertEqual(find_it([0, 1, 0, 1, 0]), 0)

if __name__ == '__main__':
    unittest.main()
