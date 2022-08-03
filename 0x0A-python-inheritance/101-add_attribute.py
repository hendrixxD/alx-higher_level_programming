#!/usr/bin/python3
"""module class for addition of attributs"""


def add_attribute(self, name, value):
    if hasattr(self, '__dict__'):
        setattr(self, name, value)
    else:
        raise TypeError("cant add new attribute")
