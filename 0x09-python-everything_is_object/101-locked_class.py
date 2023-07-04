#!/usr/bin/python3
""" a class LockedClass with no class or object attribute is defined"""


class LockedClass:
    """
    Only the  instatiation of an attribute called first_name is allowed
    """

    __slots__ = ["first_name"]
