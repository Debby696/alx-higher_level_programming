#!/usr/bin/python3
"""this module defines a Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This function represents a square"""

    def __init__(self, size):
        """A new square is initialized
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
