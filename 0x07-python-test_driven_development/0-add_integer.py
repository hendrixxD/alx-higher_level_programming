#!/usr/bin/python3
"""module that performs integers division"""

def add_integers(a, b=98):
    """Returns sum of two integers
    Args:
        a: int or float
        b: int or float

    Raises:
        TypeError: if 'a' or 'b' is not int

    Typecast: if 'a' or 'b' is float 

    """

    if not isinstance((a and b), int):
        raise TypeError("'a' must be an integer or 'b' must be an integer")
    if not isinstance((a and b), float):
        raise TypeError("'a' must be an integer or 'b' must be an integer")
    if a or b is float:
        int(a or b)
    
    return a+b

def main():
    print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

main()
