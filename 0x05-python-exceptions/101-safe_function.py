#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as ex:
        return None
        print(sys.stderr.write("Exception: {}".format(ex)))
        return None
