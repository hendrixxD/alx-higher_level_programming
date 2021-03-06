#!/usr/bin/python3
"""a module that defines coordinates of a square"""


class Square:
    """defines a square base on predesecceor module: 5-square.py"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor
        Args:
            size(int): length of side of square
            position(int): tupple of two positive numbers(points).
                           its the position of square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Raise:
            TypeError: if size is not type(int)
            ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Raise:
            TypeError: if postion is not type(int)"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value 
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Args instance: self.__size"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character '#'"""
        if self.__size == 0:
            print()
        for col in range(self.position[1]):
            print()
        for row in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
