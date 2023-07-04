#!/usr/bin/python3
"""Defines a locked class with no class or objects"""


class LockedClass:
    """
    the user is prevented from instatianting new locked attributes
    except if the new instance attribute is called first_name.
    """


    __slots__ = ["first_name"]
