#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    try:
        for item in range(x):
            print("{:d}".format(my_list[item]), end="")
            num += 1
        return num

    except (IndexError, TypeError, ValueError):
        pass
        print()
