#!/usr/bin/python3
"""
Unittest for max_integer(list)
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Class to run unittests for the max_integer function
    """

    def test_basic_max(self):
        """
        Test for basic list with integers
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_with_duplicates(self):
        """
        Test for a list with duplicated maximum values
        """
        self.assertEqual(max_integer([1, 4, 4, 2]), 4)

    def test_empty_list(self):
        """
        Test for an empty list
        """
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """
        Test for a list with a single element
        """
        self.assertEqual(max_integer([5]), 5)

    def test_max_with_negative_numbers(self):
        """
        Test for a list with negative numbers
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_with_mixed_numbers(self):
        """
        Test for a list with mixed positive and negative numbers
        """
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

if __name__ == '__main__':
    unittest.main()
