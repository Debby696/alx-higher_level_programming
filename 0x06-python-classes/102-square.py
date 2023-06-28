#!/usr/bin/python3
"""a class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """depicts a square."""

    def __init__(self, size=0):
        """a new square is initialized.

        Args:
            size (int): The new square size.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current square size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """the current area of the square is returned."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """the == comparision to a Square is defined."""
        return self.area() == other.area()

    def __ne__(self, other):
        """the != comparison to a Square is defined."""
        return self.area() != other.area()

    def __lt__(self, other):
        """the < comparison to a Square is defined."""
        return self.area() < other.area()

    def __le__(self, other):
        """the <= comparison to a Square is defined."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """the > comparison to a Square is defined."""
        return self.area() > other.area()

    def __ge__(self, other):
        """the >= comparison to a Square definition."""
        return self.area() >= other.area()
