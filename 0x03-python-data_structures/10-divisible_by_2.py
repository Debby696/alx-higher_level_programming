#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """a function that finds all multiples of 2 in a list"""
    multiples = []
    for mul in range(len(my_list)):
        if my_list[mul] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)
    return (multiples)
