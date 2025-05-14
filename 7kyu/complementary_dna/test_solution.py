import unittest
from solution import DNA_strand

class TestDNAComplement(unittest.TestCase):
    def test_basic_complement(self):
        self.assertEqual(DNA_strand("ATTGC"), "TAACG")
        self.assertEqual(DNA_strand("GTAT"), "CATA")

    def test_empty_string(self):
        self.assertEqual(DNA_strand(""), "")

    def test_single_nucleotide(self):
        self.assertEqual(DNA_strand("A"), "T")
        self.assertEqual(DNA_strand("T"), "A")
        self.assertEqual(DNA_strand("C"), "G")
        self.assertEqual(DNA_strand("G"), "C")

    def test_repeated_nucleotides(self):
        self.assertEqual(DNA_strand("AAAA"), "TTTT")
        self.assertEqual(DNA_strand("CCCC"), "GGGG")

if __name__ == '__main__':
    unittest.main()
