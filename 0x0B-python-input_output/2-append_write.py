#!/usr/bin/python3
"""This module defines a file appended to a string & return no of xter added"""


def append_write(filename="", text=""):
    """This function appends a string to the end of a UTF8 text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
