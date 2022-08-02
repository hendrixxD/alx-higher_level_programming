#!/usr/bin/python3
""" validates Exact'ness of an object"""


def is_same_class(obj, a_class):
    """returns True if 'object' is exacly an instance of specified class"""
    return (type(obj) == a_class)
