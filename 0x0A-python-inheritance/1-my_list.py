#!/usr/bin/python3
"""My List module"""


class MyList(list):
    """inherits from list class"""

    def print_sorted(self):
        """print list items in assorted order
            new_list = self[:]
            new_lisr.sort()
            print("{}".format(new_list
        """
        print(sorted(self))
