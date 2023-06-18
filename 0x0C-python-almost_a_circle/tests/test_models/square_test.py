#!/usr/bin/python3
"""Unittest module for Square class

Parameters:
    self (class)
"""
import unittest
import io
import sys


from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_square_foundations(unittest.TestCase):

    def test_is_subclass(self):
        self.assertEqual(issubclass(Square, Rectangle), True)
        
    def test_for_ids(self):
        sq = Square(9, 4, 5, 6)
        self.assertEqual(sq.id, 6)
        sq = Square(3, 2, 1, 4)
        self.assertEqual(sq.id, 4)

    #def test_for_ids(self):
        #sq = Square(8)
        #print("sq id is:", )
        #self.assertEqual(sq.id, 1)
        #sq = Square(7)
        #print("Then id is:", sq.id)
        #self.assertEqual(sq.id, 2)

    def test_for_square_area(self):
        sq = Square(5).area()
        self.assertEqual(sq, 25)

    def test_for_negative_square_area(self):
        a = [0, -1, -5]
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            for elements in a:
                sq = Square(elements)

    def test_for_unique_character(self):
        expected_output = "###\n###\n###\n"
        sq = Square(3)

        #  redirect stdout to a buffer
        stdout = io.StringIO()
        sys.stdout = stdout
        sq.display()
        sys.stdout = sys.__stdout__ #  Restore stdout
        actual_output = stdout.getvalue()
        self.assertEqual(actual_output, expected_output)

    def test_size(self):
        a = [1, 2, 3, 4, 5]
        for elements in a:
            sq = Square(elements)
        self.assertEqual(sq.size, elements)

    def test_more_size(self):
        sq = Square(9, 2, 3)
        self.assertEqual(sq.size, 9)

    def test_different_types(self):
        a = [True, None, 1.2, "1", [1, 2, 3]]
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            for items in a:
                sq = Square(items).size

    def test_empty(self):
        with self.assertRaises(TypeError):
            sq = Square()

    def test_too_many_arguments(self):
        with self.assertRaises(TypeError):
            sq = Square(1, 2, 3, 4, 7)

    def test_width_and_height(self):
        sq = Square(5, 6, 8)
        self.assertEqual(sq.width, 5)
        self.assertEqual(sq.height, 5)

    def test_x_and_y(self):
        sq = Square(9, 8, 7, 6)
        self.assertEqual(sq.x, 8)
        self.assertEqual(sq.y, 7)


class Test_square_dict(unittest.TestCase):

    def test_to_dictionary(self):
        sq = Square(10, 2, 1, 4)
        expected_output = {'id': 4, 'size': 10, 'x': 2, 'y': 1}
        self.assertDictEqual(sq.to_dictionary(), expected_output)

    def test_to_dictionary_with_args(self):
        with self.assertRaises(TypeError):
            Square(10, 2, 1, 4).to_dictionary(5)



if __name__ == '__main__':
    unittest.main()