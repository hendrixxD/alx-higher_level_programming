#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = int(a) int(b)
    except ZeroDivisionError:
        return result
    finally:
        print("Inside Result: {}".format(result))
    return result