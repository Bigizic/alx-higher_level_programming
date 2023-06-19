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
import csv
import turtle


class Base:
    """Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of list_dictionaries
        """
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON serialization of list_objs to a file, Has
        the serialization behaviour


        Make a call to (to_json_string()) function and iterate through
        the list_obj, and convert each object in the list_obj to it's
        dictionary representation using the *to_dictionary()* function
        then pass it to (to_json_string()) function, this assumes that
        the objects in list_obj are to have a *to_dictionary()*
        method/function otherwise this implementation wouldn't be possible
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as open_file:
            if list_objs is None:
                open_file.write("[]")
            else:
                string_rep = cls.to_json_string(
                        [objs.to_dictionary() for objs in list_objs])
                open_file.write(string_rep)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        """

        """Created a dummy instance, this assumes that the cls expects
        width and height if the class name is Rectangle only as
        mandatory attributes and initializes
        them to be greater than 0. The update method is then called on the
        dummy instance passing the dictionary arguments to it.
        By following this approach a new instance of the class with
        custom attributes values without explicitly specifying each
        attribute separately is created
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        else:
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        If the file doesn't exit return an empty list
        otherwise a list of instances, must use from_json_string()
        and create(). Has the deserialization behaviour
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as open_file:
                json_data = open_file.read()
                dict_list = cls.from_json_string(json_data)
                dummy_instance = [cls.create(**d) for d in dict_list]
                return dummy_instance
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """write the CSV serialization of list_objs to a file,
        Has the serialization behaviour
        """
        class_name = ["id", "width", "height", "x", "y"]
        if cls.__name__ == "Square":
            class_name = ["id", "size", "x", "y"]

        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as open_file:
            writer = csv.DictWriter(open_file, fieldnames=class_name)
            if list_objs is None or list_objs == []:
                writer.write("[]")
            else:
                for objs in list_objs:
                    writer.writerow(objs.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Mimicks the behavior of the JSON deserialization
        Return a list of classes from a CSV file
        """
        class_name = ["id", "width", "height", "x", "y"]
        if cls.__name__ == "Square":
            class_name = ["id", "size", "x", "y"]

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as open_file:
                l_d = csv.DictReader(open_file, fieldnames=class_name)
                dct = [dict([k, int(v)] for k, v in d.items()) for d in l_d]
                return [cls.create(**d) for d in dct]
        except IOError:
            return "[]"

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Both classes objects using the turtle_module

        Parameters:
            list_rectangles (list) list of rectangle object to draw
            list_squares (list) list or Square object to draw
        """
        screen = turtle.Screen()
        screen.bgcolor("black")

        def draw_rectangle(rectangle):
            t = turtle.Turtle()
            t.shape("turtle")
            t.color("white")
            t.penup()
            t.goto(rectangle.x, rectangle.y)
            t.pendown()
            for i in range(2):
                t.forward(rectangle.width)
                t.left(90)
                t.forward(rectangle.height)
                t.left(90)
            t.penup()
            t.hideturtle()

        def draw_square(square):
            t = turtle.Turtle()
            t.shape("turtle")
            t.color("white")
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for i in range(4):
                t.forward(square.size)
                t.left(90)
            t.penup()
            t.hideturtle()
        for rectangle in list_rectangles:
            draw_rectangle(rectangle)

        for square in list_squares:
            draw_square(square)

        turtle.done()
