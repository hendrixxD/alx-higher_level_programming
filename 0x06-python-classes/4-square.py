#!/usr/bin/python3
""" class modul that Access and update private attribute"""


class Square:
    """defines a square base on predecessor module: 3-square.py"""

    def __init__(self, size=0):
        """Constructor.
        Args:
            size(int): a private instance, length side of square
        """
        self.__size = size

    @property
    def size(self):
        """
        Raises:
            TypeError: if size is not type 'int'
            ValueError: if size < 0
        """

        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")


        self.__size = size

    def area(self):
        """return the area of Square"""

        return self.__size*self.__size
