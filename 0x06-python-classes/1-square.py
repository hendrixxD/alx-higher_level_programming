#!/usr/bin/python3
"""defines a Square base on '0-Square.py'"""


class Square:
    """
    square with artribute: size
    """
    def __init__(self, size):
        """
        args:
            size: private size of the square
        """
        self.__size = size
