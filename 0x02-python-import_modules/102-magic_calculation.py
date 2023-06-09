#!/usr/bin/python3
def magic_calculation(a, b):
    """Python function def magic_calculation(a, b): that does exactly the same
    as bytecode provided by holberton schol"""
    add = __import__('magic_calculation_102').add
    sub = __import__('magic_calculation_102').sub

    if a < b:
        c = add(a, b)
        for a in range(4, 6):
            c = add(c, a)
            return (c)

        else:
            return (sub(a, b))
