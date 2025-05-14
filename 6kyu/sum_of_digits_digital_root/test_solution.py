import unittest
from solution import digital_root

class TestDigitalRoot(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(digital_root(16), 7)
        self.assertEqual(digital_root(942), 6)
        self.assertEqual(digital_root(132189), 6)
        self.assertEqual(digital_root(493193), 2)

    def test_single_digit(self):
        self.assertEqual(digital_root(0), 0)
        self.assertEqual(digital_root(5), 5)

    def test_large_numbers(self):
        self.assertEqual(digital_root(999999999), 9)
        self.assertEqual(digital_root(123456789), 9)

if __name__ == '__main__':
    unittest.main()
