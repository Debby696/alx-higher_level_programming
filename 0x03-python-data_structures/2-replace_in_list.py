#!/usr/bin/python3
def replace_in_list(my_list, idx, new_element:):
    """replaces an element of a list at a specific position (like in C)."""
    if 0 <= idx < len(my_list):
        my_list[idx] = new_element
        return (my_list)