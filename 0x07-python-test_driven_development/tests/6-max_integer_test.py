#!/usr/bin/python3
"""Unittest for max_integer([..])

Parameters:
    self
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Text Cases:
        test for empty list, should return None
        test for negative numbers
        test for positive and negative numbers
        test for numbers and string expect TypeError
        test for None as argument to max_integer expect TypeError
        test for some data types expect TypeError
        test for float types
        test for positive numbers
    """
    # test for empty list, should return None
    def test_empty_list(self):
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    # test for negative numbers
    def test_negative_numbers(self):
        my_list = [-10, -12, -13, -1, -2, -6]
        self.assertEqual(max_integer(my_list), -1)

    # test for positive and negative numbers
    def test_positive_negative_numbers(self):
        my_list = [1, 100, 89, 200, -12, -56, -89]
        self.assertEqual(max_integer(my_list), 200)

    # test for numbers and string expect TypeError
    def test_numbers_and_strings(self):
        my_list = [10, 9, 98, 20, "Isaac"]
        self.assertRaises(TypeError, max_integer, my_list)

    # test for None as argument to max_integer expect TypeError
    def test_none(self):
        my_list = None
        self.assertRaises(TypeError, max_integer, my_list)

    # test for some data types expect TypeError
    def test_all_types(self):
        my_list = [1, "Isaac", 3.142, True, None]
        self.assertRaises(TypeError, max_integer, my_list)

    # test for float types
    def test_float_types(self):
        my_list = [3.14, 8.95, 1.56]
        self.assertEqual(max_integer(my_list), 8.95)

    # test for positive numbers
    def test_positive_numbers(self):
        my_list = [1, 2, 3, 4, 100, 8, 4]
        self.assertEqual(max_integer(my_list), 100)

    # test for positive numbers in reversed
    def test_positive_numbers_reversed(self):
        my_list = [4, 1, 2, 3]
        self.assertEqual(max_integer(my_list), 4)

    # test for positive infinity
    def test_positive_infinity(self):
        my_list = [1, 2, 3, float('inf'), 100]
        self.assertEqual(max_integer(my_list), float('inf'))

    # test for negative infinity
    def test_negative_infinity(self):
        my_list = [1, 2, 3, -float('inf'), 100]
        self.assertEqual(max_integer(my_list), 100)

    # test when length of list is one
    def test_when_length_of_list_is_one(self):
        my_list = [10]
        self.assertEqual(max_integer(my_list), 10 )
