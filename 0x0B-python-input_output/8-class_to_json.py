#!/usr/bin/python3
"""module tha defines a function which transforms class to JSON"""


def class_to_json(obj):
    """return the dict of a class in json format
    return json.dumps(obj.__dict__)
    """

    return obj.__dict__
