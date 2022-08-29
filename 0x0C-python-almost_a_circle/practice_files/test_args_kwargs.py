#!/usr/bin/python3

def test_args_kwargs(arg1,arg2,arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

var = ("well", 3, 4)
test_args_kwargs(*var)

name = {"arg1":"dan", "arg2":19, "arg3":"Software Enginnering"}
test_args_kwargs(**name)
