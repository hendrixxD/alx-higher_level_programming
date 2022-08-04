#!/usr/bin/python3
"""modue that reads input and returns no of char written"""


def write_file(filename="", text=""):
    """filename(str): in .txt to append texts
        text(str): text to append to filename
    """
    with open('file_append.txt', 'w+', encoding='utf-8') as f:
        size_count= f.write(text)
    return size_count
