#!/usr/bin/python3
"""module model that perform: load, add amd save"""
import json
from sys import argv


def save_to_json_file(my_obj, filename):
    """write my_obj to text file using json repr"""

    with open(filename, 'w') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """creates an object file from a json file"""
    with open(filename) as f:
        ob_file = json.load(f)
    return ob_file

filename = "add_item.json"


try:
    new_file = load_from_json_file(filename)
except (ValueError, FileNotFoundError, TypeError):
    new_file = []

new_file += argv[1:]
save_to_json_file(new_file, filename)
