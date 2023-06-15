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
        return ("[Square] ({}) {}/{} - {}" .format(self.id, self.x,
            self.y, self.width))
