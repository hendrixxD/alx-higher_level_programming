#!/usr/bin/pyhon3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
        print(sys.stderr.write("Exception: Unknown format code 'd' for object of type 'str'"))


