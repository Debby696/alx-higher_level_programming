#!/usr/bin/python3
# 4-print_square.py
""" a function that prints a square with the character #."""


def print_square(size):
    """It Print a square with the character #.

    Args:
        size (int): is the height/width of the square.
    Note:
        if size is a float and is less than 0, raise a TypeError
        if size is less than 0, raise a ValueError
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
