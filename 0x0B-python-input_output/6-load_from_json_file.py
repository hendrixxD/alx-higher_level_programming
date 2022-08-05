#!/usr/bin/python3
"""defines a module that create an object file from json file"""
import json


def load_from_json_file(filename):
    """creates an object file from a json file"""
    with open(filename) as f:
        ob_file = json.load(f)
    return ob_file
