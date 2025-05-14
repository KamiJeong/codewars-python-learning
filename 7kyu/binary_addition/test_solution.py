import unittest
from solution import add_binary

class TestAddBinary(unittest.TestCase):
    def test_basic_addition(self):
        self.assertEqual(add_binary(1, 1), "10")
        self.assertEqual(add_binary(2, 3), "101")

    def test_zero_addition(self):
        self.assertEqual(add_binary(0, 0), "0")
        self.assertEqual(add_binary(0, 5), "101")

    def test_large_numbers(self):
        self.assertEqual(add_binary(1024, 2048), "110000000000")
        self.assertEqual(add_binary(12345, 67890), bin(12345 + 67890)[2:])

if __name__ == '__main__':
    unittest.main()
