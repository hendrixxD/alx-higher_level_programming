#!/usr/bin/python3

def read_args_(arg, *argv):
    print("first normal arg:", arg)
    for arg_v in argv:
        print("another arg_v through *argv :", arg_v)

read_args_("me","and", "my", "guys")

