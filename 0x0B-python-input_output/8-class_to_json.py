#!/usr/bin/python3
"""module tha defines a function which transforms class to JSON"""
import json


def class_to_json(obj):
    return json.dumps(obj.__dict__)
