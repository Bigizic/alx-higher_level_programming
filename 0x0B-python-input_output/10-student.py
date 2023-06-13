#!/usr/bin/python3
"""A class Student that defines a student by: (based on 9-student.py)

Parameters:
    first_name (str)
    last_name (str)
    age (int)

Raises:
    void

Return:
    a dictionary representation of a Student instance
"""


class Student:
    """Class Implementation
    """

    def __init__(self, first_name, last_name, age):
        """Constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Description:
            this function checks if the attrs is a list, if yes it return
            items as a dict, by iterating through attrs and storing each
            iterated element in items then it check if the class (self)
            has an attribute in the items variable if yes it proced to
            get the attribute of that particular item from the class
            Student(self) and store it in items then it returns the
            attribute
            """
        if type(attrs) is list:
            return {items: getattr(self, items) for items in attrs
                    if hasattr(self, items)}
        else:
            return vars(self)
