#!/usr/bin/python3
"""defines a full sqaure"""


Rectangle = __import__('9-rectangle.py').Rectangle

class Square(Rectangle):
    """defines a square base on previous: 9-rectangle.py"""

    def __init__(self, size):
        """Args:
            size: private args
            size must be positive"
        """

        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """area of square"""

        return self.__size**2
