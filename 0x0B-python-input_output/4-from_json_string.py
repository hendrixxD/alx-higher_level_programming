#!/usr/bin/python3
"""module that performs JSON strings to objects"""
import json


def from_json_string(my_str):
    """retutns an object represemted by JSON string"""

    return json.loads(my_str)
