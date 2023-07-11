#!/usr/bin/python3
"""
    a function that returns the list of available attributes
    and methods of an object:
"""


def lookup(obj):
    """looks out for all attributes and methods of an object"""
    return dir(obj)
