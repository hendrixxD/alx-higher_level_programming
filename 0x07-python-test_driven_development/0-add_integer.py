#!/usr/bin/python3
"""module that performs integers addition"""


def add_integer(a, b=98):
    """Returns sum of two integers
    Args:
    a: int or float
        b: int or float
    Raises:
        TypeError: if 'a' or 'b' is not int
        Typecast: if 'a' or 'b' is float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("'a' must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("'b' must be an integer")
    return int(a) + int(b)
