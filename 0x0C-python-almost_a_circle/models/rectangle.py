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
        super().__init__(id)
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
        self.__value = y
