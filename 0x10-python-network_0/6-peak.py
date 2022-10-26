#!/usr/bin/python3
"""contains the function find_peak"""


def find_peak(list_of_int):
    """A function that finds a peak in a list of unsorted integers"""

    for i in range(len(list_of_int)):
        if i > 0 and list_of_int[i] < list_of_int[i - 1]:
            return list_of_int[i - 1]
    if list_of_int:
        return list_of_int[len(list_of_int) - 1]
