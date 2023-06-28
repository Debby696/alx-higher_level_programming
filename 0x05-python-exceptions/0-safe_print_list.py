#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """a function that prints x elements of a list

    args:
        my_list (list): is the list elements is to be printed from and can be any type.
        x (int): Depicts the number of elements of my_list to be printed.

    returns:
         the real number of elements printed
    """
    count = 0
    for a in range(x):
        try:
            print("{}".format(my_list[a]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return (count)

