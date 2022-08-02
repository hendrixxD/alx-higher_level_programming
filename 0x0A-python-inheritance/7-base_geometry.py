#!/usr/bin/python3
"""class module definition base on 6-base_geometry.py"""


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
