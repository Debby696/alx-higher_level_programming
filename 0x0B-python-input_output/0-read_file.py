#!/usr/bin/python3
"""This module defines a text file-reading function and prints to std output"""


def read_file(filename=""):
    """This prints the contents of the UTF8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
