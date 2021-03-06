#!/usr/bin/python3
"""Real definition of a rectangle module"""


class Rectangle:
    """defines a rectangle  base on previous"""

    def __init__(self, width=0, height=0):
        """Constructor:
        width(int): private instance attribute of a class
                    it is the breath of the rectangle
        height(int):private instance attribute of a class
        Raises:
        TypeError: if width is not int
                 : if height is not int
        ValueError: if width is < 0
                  : if height is < 0
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Raise:
            TypeError: if width is not int
            ValueError: if width < 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Raise:
            TypeError: if height is not type(int)
            ValueError: if height is < 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
