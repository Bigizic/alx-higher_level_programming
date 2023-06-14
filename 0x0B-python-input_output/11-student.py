#!/usr/bin/python3
"""A class Student that defines a student by: (based on 10-student.py)

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
        """Retrives a dictionary representation of Student instance
        If attrs is a list of strings, only attributes name contain in
        this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """
        if type(attrs) is list:
            return {items: getattr(self, items) for items in attrs
                    if hasattr(self, items)}
        else:
            return vars(self)

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        Description:
            if json is a dict then we iterate through json items, both
            items(key, value), if class Student(self) has the attribute
            key, set the class Student(self) public instance to value
        """
        if type(json) is dict:
            for key, value in json.items():
                if hasattr(self, key):
                    setattr(self, key, value)
