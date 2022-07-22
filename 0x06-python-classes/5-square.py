#!/usr/bin/python3
"""defines a module base on predeseccor module: '4-square.py'"""


class Square:
    """defines a square that print to stdout th square with '#'"""

    def __init__(self, size=0):
        """Constructor.
        Args:
            size(int): length of side of square
        """

        self.__size = size

    @property
    def size(self):
        """
        Raises:
            TypeError: if size is not type(int)
            ValueError: if size < 0
        """

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the area of square taking in size as attribute instance"""
        return self.__size * self.__size

    def my_print(self):
        """print:
            to stdout the square with the '#' character
            empty line if size = 0
        """
        if self.__size == 0:
            print()
        else:
            for r in range(self.__size):
                for c in range(self.__size):
                    print("#", end="\n" if c is self.__size - 1 and r != c else "")
            print()


def main():
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")

main()
