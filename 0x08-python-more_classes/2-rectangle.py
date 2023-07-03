#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)"""


class Rectangle:
    """this signifies a rectangle"""

    def __init__(self, width=0, height=0):
        """rectangle class is being initialized
        Args:
            width:is the rectangle width
            height:signifies rectangle height
        Note:
            if height is less than 0, raise a ValueError
            height must be an integer, otherwise raise a TypeError
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width attribute is retrieved"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get/set rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of  rectangle is returned"""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter of the rectangle is returned"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
