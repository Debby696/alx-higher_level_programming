#!/usr/bin/python3
if __name__ == "__main__":
    """ a program that prints the number of and the list of its arguments."""
    import sys
    len = len(sys.argv) - 1
    for i in range(len):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
    if len == 0:
        print("0 arguments")
    elif len == 1:
        print("1 arguments.")
    else:
        print("{} arguments:".format(len))
