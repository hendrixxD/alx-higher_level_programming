#!/usr/bin/python3
"""class module"""
class Square:


    """raise:
        Exception: if size is not type int
                   if size < 0
    """
    def __init__(self, size=0):

        """atrr:
            size(int): private instance
        """"
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
