#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """This Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): is the text to print.
    Note:
        text must be a string, otherwise raise a TypeError
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    d = 0
    while d < len(text) and text[d] == ' ':
        d += 1

    while d < len(text):
        print(text[d], end="")
        if text[d] == "\n" or text[d] in ".?:":
            if text[d] in ".?:":
                print("\n")
            d += 1
            while d < len(text) and text[d] == ' ':
                d += 1
            continue
        d += 1
