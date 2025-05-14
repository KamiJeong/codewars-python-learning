import unittest
from solution import get_sum

class TestGetSum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(get_sum(1, 5), 15)
        self.assertEqual(get_sum(3, 7), 25)

    def test_negative_numbers(self):
        self.assertEqual(get_sum(-3, -1), -6)
        self.assertEqual(get_sum(-5, -2), -14)

    def test_mixed_numbers(self):
        self.assertEqual(get_sum(-2, 2), 0)
        self.assertEqual(get_sum(-3, 3), 0)

    def test_single_number(self):
        self.assertEqual(get_sum(5, 5), 5)
        self.assertEqual(get_sum(-3, -3), -3)

if __name__ == '__main__':
    unittest.main()
