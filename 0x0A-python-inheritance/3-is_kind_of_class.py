#!/usr/bin/python3
"""True if obj is instance of or obj is instance of class"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: object to be tested
        a_class: class to check
    """
    if isinstance(obj, a_class):
        return True
    return False
