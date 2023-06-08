#!/usr/bin/python3
if __name__ == "__main__":
    """this prints the result of the addition of all arguments"""
    import sys
    total_sum = 0
    for a in range(1, len(sys.argv)):
        total_sum += int(sys.argv[a])
    print("{}".format(total_sum))
