#!/usr/bin/python3
def number_keys(a_dictionary):
    """returns the number of keys in a dictionary."""
    num = 0
    list_keys = list(a_dictionary.keys())

    for k in list_keys:
        num += 1
    return (num)
