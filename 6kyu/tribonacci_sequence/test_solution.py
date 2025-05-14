import unittest
from solution import tribonacci

class TestTribonacci(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(tribonacci([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
        self.assertEqual(tribonacci([0, 0, 1], 10), [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])
        self.assertEqual(tribonacci([0, 1, 1], 10), [0, 1, 1, 2, 4, 7, 13, 24, 44, 81])

    def test_edge_cases(self):
        self.assertEqual(tribonacci([1, 1, 1], 0), [])
        self.assertEqual(tribonacci([1, 1, 1], 1), [1])
        self.assertEqual(tribonacci([1, 1, 1], 2), [1, 1])
        self.assertEqual(tribonacci([1, 1, 1], 3), [1, 1, 1])

    def test_custom_signature(self):
        self.assertEqual(tribonacci([3, 2, 1], 5), [3, 2, 1, 6, 9])
        self.assertEqual(tribonacci([1, 2, 3], 6), [1, 2, 3, 6, 11, 20])

if __name__ == '__main__':
    unittest.main()
