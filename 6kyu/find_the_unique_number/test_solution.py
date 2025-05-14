import unittest
from solution import find_uniq

class TestFindUniqueNumber(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(find_uniq([1, 1, 1, 2, 1, 1]), 2)
        self.assertEqual(find_uniq([0, 0, 0.55, 0, 0]), 0.55)
        self.assertEqual(find_uniq([3, 3, 3, 7, 3, 3]), 7)

    def test_edge_cases(self):
        self.assertEqual(find_uniq([1, 1, 1, 1, 1, 0]), 0)
        self.assertEqual(find_uniq([2, 2, 2, 2, 2, 2.1]), 2.1)

    def test_no_unique(self):
        self.assertIsNone(find_uniq([1, 1, 1, 1, 1]))
        self.assertIsNone(find_uniq([]))

if __name__ == '__main__':
    unittest.main()
