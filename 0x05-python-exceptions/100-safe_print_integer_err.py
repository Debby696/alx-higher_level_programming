#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """a function that prints an integer with "{:d}".format()
    value: integer to print
    Returns:True if value has been correctly printed otherwise false."""

    try:
        print("{:d}".format(value))
        return (True)
    except(TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
