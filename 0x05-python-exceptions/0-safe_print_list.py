#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0

    try:
        for item in range(0, x):
            print("{}".format(my_list[item]), end="")
            num += 1

    except IndexError:
        pass
        #print("out of range")
    except ValueError:
        pass
        #print("my_list combined of all data types")
    print()

    return num
