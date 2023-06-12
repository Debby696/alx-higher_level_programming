#!/usr/bin/python3
def multiple_returns(sentence):
    """this returns a tuple with the length of a string
    and its first character."""
    if sentence == "":
        """If sentence is empty,first character should be equal to None"""
        return (0, None)
    return (len(sentence), sentence[0])
