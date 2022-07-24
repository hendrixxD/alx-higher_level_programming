#!/usr/bin/python3
""" class modul that compares two Squares"""


class Square:
    """defines a square base on predecessor module: 4-square.py"""

    def __init__(self, size=0):
        """Constructor.
        Args:
            size(int, float): a private instance, length side of square
        """
        self.__size = size

    @property
    def size(self):
        """
        Raises:
            TypeError: if size is not type 'int' or 'float
            ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(size, int or float):
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the area of Square"""
        return self.__size*self.__size

    def __lt__(self, other):
        return (self.area() < other.area())

    def __le__(self, other):
        return (self.area() <= other.area())

    def __eq__(self, other):
        return (self.area() == other.area())

    def __ne__(self, other):
        return (self.area() != other.area())

    def __gt__(self, other):
        return (self.area() > other.area())

    def __ge__(self, other):
        return (self.area() >= other.area())
