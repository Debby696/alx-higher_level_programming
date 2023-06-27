#!/usr/bin/python3
"""a class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """stands for a square"""


def __init__(self, size=0):
    """this will initialize a new square

    args:
    size(int): is the size of the new square
    """

    if not isinstance(size, int):
        raise TypeError
    elif size < 0:
        raise ValueError
    self.__size = size
