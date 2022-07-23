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
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")


def main():
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")

main()
