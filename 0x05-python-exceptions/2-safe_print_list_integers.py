#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        num = 0
        for item in range(0, x):
            print("{:d}".format(my_list[item]), end="")
            num += 1
        return num

    except IndexError:
        pass
    except TypeError:
        pass
        print()
