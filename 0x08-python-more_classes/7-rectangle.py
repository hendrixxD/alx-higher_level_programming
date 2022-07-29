#!/usr/bin/python3
"""change repr, prints any shape base on width ans height"""


class Rectangle:
    """defines a rectangle  base on previous"""

    number_of_instances = 0
    print_symbol = "C"

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
        Rectangle.number_of_instances += 1

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
        if self.__width == 0 and self.__height == 0:
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
            rect.append(str(self.print_symbol) * self.__width)
            if n != self.__height - 1:
                rect.append('\n')
        return ''.join(rect)

    def __repr__(self):
        """
        return a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return ("rectangle {:d} {:d}", self.__width, self.__height)

    def __del__(self):
        """print when deleting an instance of a class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
