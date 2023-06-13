#!/usr/bin/python3
"""A class Student that defines a student by:
    Public instance attributes:
        first_name
        last_name
        age

Parameters:
    first_name (str)
    last_name (str)
    age (int)

Raises:
    Void

Return:
    a dictionary representation of a Student instance
"""


class Student:
    """Class Student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of Student
        """
        return vars(self)
