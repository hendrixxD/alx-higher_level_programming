#!/usr/bin/python3
import json
"""module that returns JSON repr of an object"""


def to_json_string(my_job):
    """return the JS standard notation for the my_job object"""

    return json.dumps(my_job)
