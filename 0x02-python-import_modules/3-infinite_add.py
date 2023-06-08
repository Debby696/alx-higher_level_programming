#!/usr/bin/python3
if __name__ == "__main__":
    """this prints the result of the addition of all arguments"""
    import sys
    total_sum = 0
    for a in range(len(sys.argv) - 1):
        total_sum += int(sys.arg[a + 1])
        print("{}".format(total_sum))
