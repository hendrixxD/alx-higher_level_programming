#!/usr/bin/python3
"""module that reads from a file"""


def read_file(filename=""):
    """read from a text file
        UTF-8
        Attr: myfile.txt
    """
    
    with open('my_file_0.txt', encoding="utf-8") as f:
        """opens the file: my_file in read mode: 'r'
        with encoding: in 8-bits"""
        for line in f:
            print(line, end="")
