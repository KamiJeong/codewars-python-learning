import unittest
from solution import count_positives_sum_negatives

class TestCountPositivesSumNegatives(unittest.TestCase):
    def test_mixed_values(self):
        self.assertEqual(count_positives_sum_negatives([1, 2, 3, -1, -2, -3]), [3, -6])

    def test_all_positives(self):
        self.assertEqual(count_positives_sum_negatives([1, 2, 3, 4]), [4, 0])

    def test_all_negatives(self):
        self.assertEqual(count_positives_sum_negatives([-1, -2, -3, -4]), [0, -10])

    def test_empty_array(self):
        self.assertEqual(count_positives_sum_negatives([]), [])

    def test_no_positives(self):
        self.assertEqual(count_positives_sum_negatives([-1, -2, 0, -3]), [0, -6])

    def test_no_negatives(self):
        self.assertEqual(count_positives_sum_negatives([1, 2, 3, 0]), [3, 0])

    def test_zero_only(self):
        self.assertEqual(count_positives_sum_negatives([0, 0, 0]), [0, 0])

if __name__ == '__main__':
    unittest.main()
