#!/usr/bin/python3
""" This checks if object is an instance of a class"""


def is_same_class(obj, a_class):
    """A function that returns true if object is an instance of the
    class, otherwise return false
    """
    return (type(obj) == a_class)
