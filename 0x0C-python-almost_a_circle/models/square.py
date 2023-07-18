#!/usr/bin/python3
"""This is a module that contains a square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This depicts a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the objects attributes"""
        Rectangle().__init__(self, width, height, size, x, y, id)

        self.size = size
        self.x = x
        self.y = y
        self.id = None

    def __str__(self):
        """This gives a format for the string representation of class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(Self):
        """This gets the value of the size"""
        return self.__width

    @size.setter
    def size(self, value):
        """This sets the value for size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Updates square by adding public method that assigns attributes"""

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if input != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

        def to_dictionary(self):
            """This returns the dictionary representation of a Square"""

            obj_dictionary = {'id': self.id, 'size': self.size, 'x': self.x,
                              'y': self.y}
            return obj_dictionary
