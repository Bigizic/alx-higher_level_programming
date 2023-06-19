#!/usr/bin/python3
"""Class Module
A Class Square that inherits from Rectangle

Parameters:
    size (int) size of the square
    x (int)
    y (int)
    id (int)

Raises:
    Void

Return:
    Void
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A subclass of a subclass
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>
        """
        my_w = self.width
        my_x = self.x
        my_y = self.y
        return ("[Square] ({}) {}/{} - {}" .format(self.id, my_x, my_y, my_w))

    @property
    def size(self):
        """Getter for size, retrives width
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """Setter for size, sets the width to a value and height
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes
        """
        length = len(args)
        count = 0
        cnt = 0
        if not args and len(args) < 1:
            for key, value in kwargs.items():
                if key is 'id' and value is None:
                    count += 1
                    value = count
                    setattr(self, key, value)
                if hasattr(self, key):
                    setattr(self, key, value)

        if (args):
            if length >= 1:
                self.id = args[0]
            if length >= 2:
                self.width = args[1]
            if length >= 3:
                self.x = args[2]
            if length >= 4:
                self.y = args[3]

    def to_dictionary(self):
        """Returns the dictionary representation of a Square Class
        """
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
