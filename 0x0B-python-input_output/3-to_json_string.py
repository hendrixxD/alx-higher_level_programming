#!/usr/bin/python3
"""module that returns JSON repr of an object"""
import json


def to_json_string(my_job):
    """returns an object (Python data structure) represented by a JSON string"""

    return json.dumps(my_job)
