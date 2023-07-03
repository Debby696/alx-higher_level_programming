#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by: (based on 5-rectangle.py)"""


class Rectangle:
    """signifies a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """a new rectangle is initialized
        Args:
            width: rectangle's width
            height: rectangle's height
        Note:
            if width is less than 0, raise a ValueError
            if height is less than 0, raise a ValueError
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """height attribute is retrieved"""
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
        """perimeter of the rectangle is returned"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """a diagramatic representation of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """the string representation of the rectangle is returned"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message for every rectangle deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
