#!/usr/bin/python3
"""magic class module"""
import math


class MagicClass:
    """bytecode interpretation"""

    def __init__(self, radius=0):
        """Constructor.
        Args:
            RADIUS;radius of circle
        """
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """return area of a circle"""
        return math.pi * self.__radius * self.__radius

    def circumference(self):
        """returns the circimference of circle"""
        return 2 * math.pi * self.__radius
