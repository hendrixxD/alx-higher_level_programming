#!/usr/bin/python3
"""module that returns JSON repr of an object"""
import json


def to_json_string(my_job):
    """return the JS standard notation for the my_job object"""

    return json.dumps(my_job)
