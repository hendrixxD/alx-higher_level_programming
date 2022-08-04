#!/usr/bin/python3
"""module that defines a fuction to append 
    a string to a file and return its size"""


def append_write(filename="", text=""):
    """appends a string; text to a file: text"""

    with open(filename, 'a', encoding='utf=8') as f:
        char_count = f.write(text)
    return char_count
