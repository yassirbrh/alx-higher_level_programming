#!/usr/bin/python3

""" add_integer - Function
    @a: First number
    @b: Second number (Initially 98)
    Return: The result
"""


def add_integer(a, b=98):

    """
        Adds two integers and returns the result.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(int(a) + int(b))
