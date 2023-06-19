#!/usr/bin/python3
"""Unittest module for Rectangle Class

Parameters:
    self (class)
"""

import unittest
import io
import sys


from models.base import Base
from models.rectangle import Rectangle


class Test_rectangle_foundations(unittest.TestCase):

    def test_rectangle_subclass(self):
        self.assertEqual(issubclass(Rectangle, Base), True)

    def test_rect_id(self):
        rect = Rectangle(10, 2)
        self.assertEqual(rect.id, 1)
        rect = Rectangle(2, 10)
        self.assertEqual(rect.id, 2)
        rect = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rect.id, 12)

    def test_rect_errors(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect = Rectangle(10, "2")
