#!/usr/bin/python3
"""modue that reads input and returns no of char written"""


def write_file(filename="", text=""):
    """filename(str): in .txt to append texts
        text(str): text to append to filename
    """

    with open('filename', 'r+', encoding='utf-8') as f:
        f.write(text)
