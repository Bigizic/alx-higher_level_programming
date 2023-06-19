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

    def setUp(self):
        super().setUp()
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

    def setUp(self):
        super().setUp()
        Base._Base__nb_objects = 0

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

    def setUp(self):
        super().setUp()
        Base._Base__nb_objects = 0

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

    def setUp(self):
        super().setUp()
        Base._Base__nb_objects = 0
    
    def test_correct_str_method_with_no_id(self):
        rect = Rectangle(5, 5, 1)
        self.assertEqual(rect.__str__(), "[Rectangle] (1) 1/0 - 5/5")

    def test_correct_str_print(self):
        rect = Rectangle(4, 6, 2, 1)
        exe_output = "[Rectangle] (1) 2/1 - 4/6\n"

        stdout = io.StringIO()
        sys.stdout = stdout
        print(rect)
        sys.stdout = sys.__stdout__
        actual_output = stdout.getvalue()
        self.assertEqual(actual_output, exe_output)


class Test_rectangle_update_function(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_update_no_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_one_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_two_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_three_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_four_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_all_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_too_many_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(9, 4, 18, 4, 5, 9, 8, 7, "Betty")
        self.assertEqual(str(r1), "[Rectangle] (9) 4/5 - 4/18")


class Test_rectangle_update_kwargs(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_update_no_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_one_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")

    def test_update_two_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/10")

    def test_update_three_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/10")

    def test_update_all_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/3 - 4/2")

    def test_update_too_many_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(x=1, height=2, y=3, width=4, id=90, size=78)
        self.assertEqual(str(r1), "[Rectangle] (90) 1/3 - 4/2")


class Test_rectangle_to_dictionary(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_to_dict(self):
        r1 = Rectangle(10, 2, 1, 9)
        exe_output = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        rect = r1.to_dictionary()
        self.assertDictEqual(rect, exe_output)
        r2 = Rectangle(1, 1)
        r2.update(**rect)
        self.assertNotEqual(r1, r2)


if __name__ == '__main__':
    unittest.main()
