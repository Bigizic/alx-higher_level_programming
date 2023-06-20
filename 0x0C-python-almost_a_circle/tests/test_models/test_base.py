#!/usr/bin/python3
"""Unittest module for Base Class

Parameters:
    self (clas)
"""

import unittest
import io
import sys


from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test_base_fundamentals(unittest.TestCase):
    """This Class contains test for the basic implementation of the Base
    class

    Tests:
        For correct Base id
    """

    def setUp(self):
        """Setup
        """
        Base._Base__nb_objects = 0

    def test_base_ids(self):
        """Ids
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)


class Test_base_to_json_string(unittest.TestCase):
    """Tests are:
        Test for correct type
        Test for length of text
        Test for empty list exceptes []
        """

    def setUp(self):
        """Setup
        """
        Base._Base__nb_objects = 0

    def test_to_json_string_type(self):
        """Json String
        """
        r1 = Rectangle(10, 7, 2, 8, 24)
        sq = Square(2, 1, 2, 42)
        self.assertEqual(str, type(
            Base.to_json_string([r1.to_dictionary()])))
        self.assertEqual(str, type(
            Base.to_json_string([sq.to_dictionary()])))

    def test_to_json_string_length(self):
        """Json string length
        """
        r1 = Rectangle(10, 7, 2, 8, 24)
        dct = [r1.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dct)) == 54)

    def test_to_json_multiple_dictionary(self):
        """Test multiple dictionareis
        """
        r1 = Rectangle(2, 4, 1, 2, 42)
        sq = Square(2, 1, 2, 42)

        dct = [r1.to_dictionary(), sq.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dct)) == 92)

    def test_to_json_string_empty_list(self):
        """Test empty list
        """
        self.assertEqual(Base.to_json_string([]), '[]')


class Test_base_save_to_file(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_save_to_file(self):
        pass


if __name__ == '__main__':
    unittest.main()
