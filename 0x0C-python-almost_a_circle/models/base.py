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
import os


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
        """Returns the JSON representation of list_dictionaries
        """
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of list_objs to a file
        """
        if not list_objs:
            return

        """
        make a call to (to_json_string()) function and iterate through
        the list_obj, and convert each object in the list_obj to it's
        dictionary representation using the *to_dictionary()* function
        then pass it to (to_json_string()) function, this assumes that
        the objects in list_obj are to have a *to_dictionary()*
        method/function otherwise this implementation wouldn't be possible
        """

        string_rep = cls.to_json_string([objects.to_dictionary()
            for objects in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, "w") as open_file:
            open_file.write(string_rep)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return ("[]")
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        """

        """Created a dummy instance, this assumes that the cls expects
        width and height only as mandatory attributes and initializes
        them to be greater than 0. The update method is then called on the
        dummy instance passing the dictionary arguments to it.
        By following this approach a new instance of the class with
        custom attributes values without explicitly specifying each
        attribute separately is created
        """
        dummy_instance = cls(1, 2)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        If the file doesn't exit return an empty list
        otherwise a list of instances, must use from_json_string()
        and create()
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        else:
            with open(filename, "r") as open_file:
                json_data = open_file.read()
                dict_list = cls.from_json_string(json_data)
                dummy_instance = [cls.create(**d) for d in dict_list]
                return dummy_instance

