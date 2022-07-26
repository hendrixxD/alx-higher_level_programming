#!/usr/bin/python3
"""module that prints a name"""

def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name
        last_name(str)

    Raises:
        TypeError: if first_name and last_name is not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name)
