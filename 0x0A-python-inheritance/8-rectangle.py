#!/usr/bin/python3
"""This module contains a class with public instance
    and Raises exception when required """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
