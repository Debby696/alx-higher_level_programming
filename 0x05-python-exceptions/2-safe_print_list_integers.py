#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """a function that prints the first x elements of a list and only integers.
    my_list: list to print the elements from
    x represents the number of elements to access in my_list
    Returns:no of elements printed
    """

    count = 0
    for a in range(0, x):

        try:
            if isinstance(my_list[a], int):
                print("{:d}".format(my_list[a]), end="")
                count += 1
        except (ValueError, TypeError):
            continue
        print("")
        return(count)
