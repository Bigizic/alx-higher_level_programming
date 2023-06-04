#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    #test for empty list, should return None
    def test_empty_list(self):
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    #test for negative numbers
    def test_negative_numbers(self):
        my_list = [-10, -12, -13, -1, -2, -6]
        self.assertEqual(max_integer(my_list), -1)

    #test for positive and negative numbers
    def test_positive_negative_numbers(self):
        my_list = [1, 100, 89, 200, -12, -56, -89]
        self.assertEqual(max_integer(my_list), 200)

    #test for numbers and atring except TypeError
    def test_numbers_and_strings(self):
        my_list = [10, 9, 98, 20, "Isaac"]
        self.assertRaises(TypeError, max_integer, my_list)

    #test for None as argument to max_integer
    def test_none(self):
        my_list = None
        self.assertRaises(TypeError, max_integer, my_list)
