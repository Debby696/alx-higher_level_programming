#!/usr/bin/python3
"""A class Rectangle that inheris from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """A new Rectangle is initialized
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
