#!/usr/bin/python3
"""A square module that defines an area of square"""


class Square:
    """defines a square base on predeseccor module: 2-square.py"""

    def __init__(self, size=0):
        """
        Constructor.

        Args:
            size(int): a private instance, length side of square
        Raises:
            TypeError: if size is not type 'int'
            ValueError: if size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the area of square"""

        return self.__size * self.__size
