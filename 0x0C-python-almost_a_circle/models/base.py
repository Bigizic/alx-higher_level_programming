#!/usr/bin/python3
"""Class Module
This class will be the base of other classes in this project, The goal of
it is to manage id attribute and to avoid duplicating the same code.

Parameters:
    id (int)

Raises:
    Void

Return:
    Void
"""

import json


class Base:
    """Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return ("[]")
        else:
            return json.dumps(list_dictionaries)
