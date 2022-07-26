#!/usr/bin/python3
"""a module that prints a square"""

def print_square(size):
    """
    Args:
        size(int): size of the square
    Raises:
        TypeError: if size is not intt
                 : if size is float and < 0
        ValueError: if size < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        print(print("{}\n".format("#" * size) * size, end=""))
