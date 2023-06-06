#!/usr/bin/python3
def uppercase(str):
    """prints a string in uppercase followed by a new line"""
    for char in str:
        if ord(c) >= 97 and ord(c) <= 122:
            char = chr(ord(c) - 32)
            print("{}".format(char), end="")
            print("")
