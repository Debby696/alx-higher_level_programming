#!/usr/bin/python3
"""This module writes  a string to a text file (UTF8) & returns no of xter"""


def write_file(filename="", text=""):
    """It writes a string to a UTF8 text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
