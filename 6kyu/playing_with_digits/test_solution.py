import unittest
from solution import dig_pow

class TestDigRow(unittest.TestCase):
    def test_valid_cases(self):
        self.assertEqual(dig_pow(89, 1), 1)
        self.assertEqual(dig_pow(695, 2), 2)
        self.assertEqual(dig_pow(46288, 3), 51)

    def test_invalid_cases(self):
        self.assertEqual(dig_pow(92, 1), -1)
        self.assertEqual(dig_pow(123, 2), -1)

    def test_edge_cases(self):
        self.assertEqual(dig_pow(1, 1), 1)
        self.assertEqual(dig_pow(0, 1), -1)

if __name__ == '__main__':
    unittest.main()
