#!/usr/bin/python3
"""Rectangle Module"""


class BaseGeometry:
    """defines a class base on previous"""

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

        self.integer_validator("width", width)
        self.integer_validator("height", height)
