#!/usr/bin/python3
if __name__ == "__main__":
    """this is to help print the sum of 1 & 2"""
    from modules.add_0 import add
    """assign values to variable a & b"""

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
