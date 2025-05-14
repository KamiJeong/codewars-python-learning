import unittest
from solution import unique_in_order

class TestUniqueInOrder(unittest.TestCase):
    def test_string_input(self):
        self.assertEqual(unique_in_order("AAAABBBCCDAABBB"), ['A', 'B', 'C', 'D', 'A', 'B'])
        self.assertEqual(unique_in_order("ABBCcAD"), ['A', 'B', 'C', 'c', 'A', 'D'])

    def test_list_input(self):
        self.assertEqual(unique_in_order([1, 2, 2, 3, 3]), [1, 2, 3])
        self.assertEqual(unique_in_order(['A', 'A', 'B', 'B', 'C']), ['A', 'B', 'C'])

    def test_empty_input(self):
        self.assertEqual(unique_in_order(""), [])
        self.assertEqual(unique_in_order([]), [])

    def test_single_element(self):
        self.assertEqual(unique_in_order("A"), ['A'])
        self.assertEqual(unique_in_order([1]), [1])

if __name__ == '__main__':
    unittest.main()
