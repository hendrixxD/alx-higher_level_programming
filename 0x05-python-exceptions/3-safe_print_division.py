#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = int(a) int(b)
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside Result: {}".format(result))
    return result
