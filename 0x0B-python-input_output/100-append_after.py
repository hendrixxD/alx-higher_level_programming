#!/usr/bin/python3
"""module that search and update a file a file"""


def append_after(filename="", search_string="", new_string=""):
    """open a file for reading"""
    with open(filename, 'r', encoding='utf-8') as f:
        newtxt = []
        lines = f.readlines()
        for line in lines:
            newtxt.append(line)
            if search_string in line:
                newtxt.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        """open a file form writing a formated text"""
        newtxt = "".join(newtxt)
        f.write(newtxt)
