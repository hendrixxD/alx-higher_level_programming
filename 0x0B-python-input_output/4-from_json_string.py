#!/usr/bin/python3i
import json
"""module that performs JSON strings to objects"""


def from_json_string(my_str):
    """retutns an object represemted by JSON string"""

    return json.load(my_str)
