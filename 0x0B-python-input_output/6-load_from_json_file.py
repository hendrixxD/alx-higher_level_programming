#!/usr/bin/python3
"""defines a module that create an object file from json file"""
import json


def load_from_json_file(filename):
    with open(filename) as f:
        return json.load(f)
