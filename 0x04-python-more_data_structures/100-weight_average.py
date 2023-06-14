#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns weighted average of all integers tuple (<score>, <weight>)"""
    if not my_list:
        return 0
    num = 0
    dec = 0

    for tup in my_list:
        num += tup[0] * tup[1]
        dec += tup[1]

    return (num / dec)
