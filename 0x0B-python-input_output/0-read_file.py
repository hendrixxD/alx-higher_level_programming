#!/usr/bin/python3
"""module that reads from a file"""


def read_file(filename=""):
    """read from a text file
        UTF-8
        Attr: myfile.txt
    """

    f = open('my_file_0.txt', 'r', encoding="utf-8")
    print(f.read())
    f.close
