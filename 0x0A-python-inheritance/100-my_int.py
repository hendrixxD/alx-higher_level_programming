#!/usr/bin/python3
"""MyInt module which inherits from int"""


class MyInt(int):
    """base class: MyInt
       int: subclass
    """

    def __eq__(self, other):
        """return invertion of =="""

        return int.__ne__(self, other)

    def __ne__(self, other):
        """return invertion of !="""

        return int.__eq__(self, other)
