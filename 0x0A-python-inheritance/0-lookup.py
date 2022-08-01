#!/usr/bin/python3
"""module: get attribute and methods of an object"""


def lookup(obj):
    """returns attributs and methods"""
    return list(dir(obj))
