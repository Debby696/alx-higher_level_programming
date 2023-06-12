#!/usr/bin/python3
def no_c(my_string):
    """a function that removes all characters c and C from a string."""
    char = [ch for ch in my_string if ch != 'c' and ch != 'C']
    return ("".join(char))
