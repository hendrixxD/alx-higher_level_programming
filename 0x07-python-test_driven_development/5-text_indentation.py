#!/usr/bin/python3
"""Text indentation module"""

def text_indentation(text):
    """prints a text with two new lines after each characters . ? and :
    Args:
        size(str): sting
    Raise:
    TypeError: "text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    string = "".join([a if a not in ".?:" else a + "\n\n" for a in text])
    print("\n".join([x.strip() for x in string.split("\n")]), end="")
