#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(len(my_list)):
        if idx < 0:
            print("{}".format(None))
        elif idx > len(my_list):
            print("{}}".format(None))
        else:
            if i == idx:
                print("{}".format(my_list[i]))
