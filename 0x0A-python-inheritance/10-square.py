#!/usr/bin/python3
"""defines a full sqaure"""


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


class Square(Rectangle):
    """defines a square base on previous: 9-rectangle.py"""

    def __init__(self, size):
        """Args:
            size: private args
            size must be positive"
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of square"""

        return self.__size**2
