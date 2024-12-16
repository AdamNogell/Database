#!/usr/bin/env python3

import unittest
from wt import WaveletTree

'''
Run test using command python -m unittest basic.py
'''

class TestWT(unittest.TestCase):
    def setUp(self):
        """initialize a sample wavelet tree for testing."""
        self.data = "banana"
        self.tree = WaveletTree(self.data)

    def test_rank(self):
        """Test the rank function of the wavelet tree."""
        self.assertEqual(self.tree.rank(0,'b'), 1)  # 'b' at index 0
        self.assertEqual(self.tree.rank(1,'a'), 1)  # 'a' at index 1
        self.assertEqual(self.tree.rank(2,'n'), 1)  # 'n' at index 2
        self.assertEqual(self.tree.rank(3,'a'), 2)  # 'a' at index 3
        self.assertEqual(self.tree.rank(4,'n'), 2)  # 'n' at index 4
        self.assertEqual(self.tree.rank(5,'a'), 3)  # 'a' at index 5

    def test_select(self):
        """Test the select function of the wavelet tree."""
        self.assertEqual(self.tree.select(1,'a'), 1)  # First occurrence of 3
        self.assertEqual(self.tree.select(2,'a'), 3)  # Second occurrence of 3
        self.assertEqual(self.tree.select(3,'a'), 5)  # First occurrence of 5

        self.assertEqual(self.tree.select(1,'n'), 2)  # First occurrence of 1
        self.assertEqual(self.tree.select(2,'n'), 4)  # Second occurrence of 1

if __name__ == '__main__':
    # unittest.main()
    WaveletTree("TEST")