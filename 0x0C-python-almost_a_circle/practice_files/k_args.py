#!/usr/bin/python3
#usage of kwargs

def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

def main():
    kwargs ={"name":"dan", "age":20, "level":"100L", "Status":"alx SE Student"}
    kw = test_args_kwargs(**kwargs)
    print(kw)
main()

