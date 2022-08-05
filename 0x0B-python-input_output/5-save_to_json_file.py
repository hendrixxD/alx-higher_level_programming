#!/usr/bin/python3
"""defines a module that writes an object file to a text file using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """write my_obj to text file using json repr"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
