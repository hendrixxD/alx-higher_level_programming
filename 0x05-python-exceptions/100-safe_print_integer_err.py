#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
        try:
            print("{:d}".format(value))
            return True
        except (TypeError, ValueError):
            return False
            print(sys.stderr.write("Exception:unkown format code 'd' for type 'str'"))
            print("Exception: Unknown format code 'd' for type 'str'", file=sys.stderr)

