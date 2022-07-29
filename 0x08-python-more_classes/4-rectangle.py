#!/usr/bin/python3
"""added repr to class"""


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
        self.__height = height

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
            raise ValueError("height must be greater or __eq__ t0 zero")
        self.__height = value

    def area(self):
        """returns the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the total length of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns string of Rectangle using #
        if 0 returns empty string
        """

        if self.width == 0 or self.height == 0:
            return ("")
        rect = []
        for n in range(0, self.__height):
            rect.append("#" * self.__width)
            if n != self.__height - 1:
                rect.append('\n')
        return ''.join(rect)

    def __repr__(self):
        """
        return a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return '{self.__class__.__name__}({self.width}, {self.height})'.\
            format(self=self)
