#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints x  elements of a list
    args:
    my_list: list to print elements from and can contain integer, string.
    x represents the number of elements to print

    Returns the real number of elements printed."""

    count = 0
    for a in range(x):
        try:
            print("{}".format(my_list[a]), end="")
            count += 1
        except IndexError:
            break
        print("")
        return(count)
