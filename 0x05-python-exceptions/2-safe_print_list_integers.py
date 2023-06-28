#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.

    Args:
        my_list (list): This is the list to print elements from.
        x (int): represents the number of elements to access in my_list

    Returns:
        the real number of integers printed
    """
    count = 0
    for a in range(0, x):
        try:
            print("{:d}".format(my_list[a]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (count)
