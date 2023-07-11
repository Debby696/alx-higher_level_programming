#!/usr/bin/python3
"""This module is a class that inherits from the list class"""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """This prints a sorted list"""
        print(sorted(self))
