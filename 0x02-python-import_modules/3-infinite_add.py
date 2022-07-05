#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_count = 0
    for i in range(1, len(argv)):
        arg_count += int(argv[i])
    print("{}".format(arg_count))
