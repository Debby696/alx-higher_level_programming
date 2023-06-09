#!/usr/bin/python3
"""a class Square that defines a square by: (based on 6-square.py)"""


class Square:
    """depicts a square."""

    def __init__(self, size=0, position=(0, 0)):
        """ a new square is initialized.

        Args:
            size (int): The new square size.
            position (int, int): The new square position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set size of the square presently."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the square position presently."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """current square area is returned."""
        return (self.__size * self.__size)

    def my_print(self):
        """that prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return

        [print("") for a in range(0, self.__position[1])]
        for a in range(0, self.__size):
            [print(" ", end="") for b in range(0, self.__position[0])]
            [print("#", end="") for c in range(0, self.__size)]
            print("")

    def __str__(self):
        """This defines the print() illustration of a Square."""
        if self.__size != 0:
            [print("") for a in range(0, self.__position[1])]
        for a in range(0, self.__size):
            [print(" ", end="") for b in range(0, self.__position[0])]
            [print("#", end="") for c in range(0, self.__size)]
            if a != self.__size - 1:
                print("")
        return ("")
