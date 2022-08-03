#!/usr/bin/python3
"""defines a square that inherits from previous claesses"""

Rectangle = __import__('9-rectangle').Rectangle
"""importing Rectangle class"""


class Square(Rectangle):
    """inherits from Rectangle clss form modification: area() and __str__()"""

    def __init__(self, size):
        """Args: private instance of class"""

        Rectangle.integer_validator(self, "size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """returns area of sqaure"""

        return self.__size * self.__size

    def __str__(self):
        """returns the description: [Square] <width>/<height>"""

        return f"[Square] {self.__size}/{self.__size}"
