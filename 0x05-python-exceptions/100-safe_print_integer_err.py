#!/usr/bin/pyhon3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
        print("Exception: Unknown format code 'd' for object of type 'str'", file=sys.stderr)





