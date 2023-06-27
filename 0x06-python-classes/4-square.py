#!/usr/bin/python3
"""a class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """stands for a square"""

    def __init__(self, size=0):
        """This initialize a new square.

        Args:
            size (int): The new square size.
        """
        self.size = size

    @property
    def size(self):
        """Get/set is the size of the square currently."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """that returns the current square area"""
        return (self.__size * self.__size)
