import unittest
from solution import delete_nth

class TestDeleteNth(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(delete_nth([1, 1, 1, 1], 2), [1, 1])
        self.assertEqual(delete_nth([20, 37, 20, 21], 1), [20, 37, 21])
        self.assertEqual(delete_nth([1, 2, 3, 1, 2, 1, 2, 3], 2), [1, 2, 3, 1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(delete_nth([], 2), [])
        self.assertEqual(delete_nth([], 0), [])

    def test_no_limit(self):
        self.assertEqual(delete_nth([1, 2, 3, 4], 0), [])
        self.assertEqual(delete_nth([1, 2, 3, 4], -1), [])

    def test_large_list(self):
        self.assertEqual(delete_nth([1] * 1000, 3), [1, 1, 1])

if __name__ == '__main__':
    unittest.main()
