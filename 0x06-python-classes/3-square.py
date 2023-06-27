#!/usr/bin/python3
"""a class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """This stands for a square."""

    def __init__(self, size=0):
        """This initializes a new square.

        Args:
            size (int): This tells us this is the size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ that returns the current square area"""
        return (self.__size * self.__size)
