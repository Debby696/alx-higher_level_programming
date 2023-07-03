#!/usr/bin/python3
""" a class Rectangle that defines a rectangle"""


class Rectangle:
    """this signifies a rectangle"""

    def __init__(self, width=0, height=0):
        """ here a new rectangle is initialized
        Args:
            width: this is the width of the new rectangle
            height: this is the height of the new rectangle
        Raises:
            height must be an integer, otherwise raise a TypeError
            if width is less than 0, raise a ValueError
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """the width of rectangle is get or set """
        return self.__width

    @width.setter
    def width(self, value):
        """this sets attribute of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get/set rectangle height """
        return self.__height

    @height.setter
    def height(self, value):
        """sets attribute of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
