#!/usr/bin/python3
"""prints the ASCII alphabet, in reverse order, alternating lowercase
and uppercase, not followed by a new line"""
a = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - a)), end="")
    a = 32 if a == 0 else 0
