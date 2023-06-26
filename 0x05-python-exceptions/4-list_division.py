#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """a function that divides element by element 2 lists.
    my_list_1: is the first list
    my_list_2: is the second list
    list_length (int):the number of elements to divide
    Returns a new list (length = list_length) with all divisions"""

    new_list = []
    try:
        for a in range(0, list_length):
            try:
                div = my_list_1[a]/my_list_2[a]
            except TypeError:
                print("wrong type")
                div = 0
            except ZeroDivisionError:
                print("division by 0")
                div = 0
            except IndexError:
                print("out of range")
                div = 0
            finally:
                new_list.append(div)
        return (new_list)
