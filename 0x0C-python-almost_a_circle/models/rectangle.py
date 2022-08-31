#!/usr/bin/python3
"""class 'Rectangle' inherits from the base class 'Base'"""


from models.base import Base


class Rectangle(Base):
    """private instance attributes:
    __width
    __height
    __x
    __y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """private instance attribute getter
        return the width of a rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """
        setter instance attribute for width
        assign value to width
        """
        if not isinstance(value, int):
            raise TypeError(f"{value} must be an integer")
        if value <= 0:
            raise ValueError(f"{value} must be > 0")
        self.__value = width

    @property
    def height(self):
        """
        private instance attribute getter
        return the height of a rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter function for height
        assigns value to height
        """
        if not isinstance(value, int):
            raise TypeError(f"{value} must be an integer")
        if value <= 0:
            raise ValueError(f"{value} must be > 0")
        self.__value = height

    @property
    def x(self):
        """
        getter function for x
        return the x value of a rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter function for x
        assigns value to x
        """
        if not isinstance(value, int):
            raise TypeError(f"{value} must be an integer")
        if value < 0:
            raise ValueError(f"{value} must be >= 0")
        self.__value = x

    @property
    def y(self):
        """
        getter function for y value
        return the y value of a rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter function for y, assign value to y
        """
        if not isinstance(value, int):
            raise TypeError(f"{value} must be an integer")
        if value < 0:
            raise ValueError(f"{value} must be >= 0")
        self.__value = y
