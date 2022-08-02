#!/usr/bin/python3
"""validates inheritance of a class"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: object to test if is instance directly/indirectly
        a_class: class to be acted upon
    """

    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
