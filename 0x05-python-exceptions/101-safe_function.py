#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """a function that executes a function safely.
    fct: is the function to be executed
    @args: is the arguments for fct
    Return: the result of the function,
    otherwise None if something happens during the function and
    prints in stderr the error precede by Exception:"""

    try:
        result = fct(*args)
        return (result)
    except Exception as e:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
