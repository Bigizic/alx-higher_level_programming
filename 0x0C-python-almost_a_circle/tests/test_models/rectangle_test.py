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

    def setup(self):
        Base._Base__nb_objects = 0

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg_missing(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(9, 8, 7, 6, 5, 4)

    def test_rectangle_subclass(self):
        self.assertEqual(issubclass(Rectangle, Base), True)

    def test_rect_id(self):
        rect = Rectangle(10, 2)
        self.assertEqual(rect.id, 1)
        rect = Rectangle(2, 10)
        self.assertEqual(rect.id, 2)
        rect = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rect.id, 12)

    def test_retrive_att(self):
        r = Rectangle(6, 5, 4, 3, 2)
        self.assertEqual(r.width, 6)
        r.width = 12
        self.assertEqual(r.width, 12)

    def test_retrive_attri(self):
        r = Rectangle(5, 8, 9, 3, 2)
        self.assertEqual(r.height, 8)
        r.height = 90
        self.assertEqual(r.height, 90)

    def test_retrive_attribut(self):
        r = Rectangle(8, 9, 3, 4, 5)
        self.assertEqual(r.x, 3)
        r.x = 80
        self.assertEqual(r.x, 80)

    def test_retrive_attributes(self):
        r = Rectangle(8, 9, 4, 3, 9)
        self.assertEqual(r.y, 3)
        r.y = 40
        self.assertEqual(r.y, 40)


class Test_Rectangle_errors(unittest.TestCase):

    def test_type_err(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect = Rectangle("Betty", 8, 7, 6, 5)

    def test_type_erro(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect = Rectangle(9, "Betty", 8, 7, 6)

    def test_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect = Rectangle(9, 8, "Betty", 7, 6)

    def test_type_errors(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect = Rectangle(10, 34, 8, "Betty", 9)

    def test_value_err(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect = Rectangle(0, 1, 2, 3, 4)

    def test_value_erro(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect = Rectangle(1, 0, 3, 4, 5)

    def test_value_error(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect = Rectangle(1, 2, -1, 4, 5)

    def test_value_errors(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect = Rectangle(1, 2, 3, -1, 8)


class Test_rectangle_fundamentals(unittest.TestCase):

    def setup(self):
        Base._Base.__nb_objects = 0

    def test_areas(self):
        rect = Rectangle(3, 2)
        self.assertEqual(rect.area(), 6)
        rect = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rect.area(), 56)

    def test_display(self):
        rect = Rectangle(4, 6)
        exe_output = "####\n####\n####\n####\n####\n####\n"

        stdout = io.StringIO()
        sys.stdout = stdout
        rect.display()
        sys.stdout = sys.__stdout__
        act_output = stdout.getvalue()
        self.assertEqual(act_output, exe_output)

    def test_display_five_arguments(self):
        rect = Rectangle(2, 2, 3, 4, 5)
        exe_output = "\n\n\n\n   ##\n   ##\n"

        stdout = io.StringIO()
        sys.stdout = stdout
        rect.display()
        sys.stdout = sys.__stdout__
        act_output = stdout.getvalue()
        self.assertEqual(act_output, exe_output)

    def test_correct_str(self):
        rect = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(rect), "[Rectangle] (12) 2/1 - 4/6")


class Test_rectangle_str_function(unittest.TestCase):

    def setup(self):
        Base._Base.__nb_objects = 0
    
    def test_correct_str_with_no_id(self):
        rect = Rectangle(5, 5, 1)
        exe_output = "[Rectangle] (1) 1/0 - 5/5"
        
        self.assertEqual(str(rect), exe_output)
