#!/usr/bin/python3
"""This module contains a class with public instance
    and Raises exception when required
    class module definition base on 6-base_geometry.py
"""


class BaseGeometry:
    """integer validator"""

    def area(self):
        """No Args passed"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value entries"""
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """inherits from baseclass: BaseGeometry
       -private attributes: width and height
    """
    def __init__(self, width, height):
        """instantiation of class"""
        self.__width = width
        self.__height = height

        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

    def area(self):
        """returns the area of the the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """returns [Rectangle] <width>/<height> description"""
        return f"[Rectangle] {self.__width}/{self.__height}"
