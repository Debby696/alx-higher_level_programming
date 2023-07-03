#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)"""


class Rectangle:
    """signifies a rectangle"""

    def __init__(self, width=0, height=0):
        """rectangle class is being initialized
        Args:
            width: this represents rectangle's width
            height: this represents rectangle's height
        Note:
            height must be an integer, otherwise raise a TypeError
            if width is less than 0, raise a ValueError
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get/set the rectangle's width"""
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
        """get/set therectangle's height"""
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
        """area of the rectangle is returned"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Perimeter of the rectangle is returned"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """ this returns the rectangle diagram that is printable"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)
