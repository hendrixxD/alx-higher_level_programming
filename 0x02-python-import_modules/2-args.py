#!/usr/bin/python3
def Argv(argv):
    for i in range(1, len(argv)):
        if i == 0:
            print("{:d} arguments.".format(i))
        elif i == 1:
            print("{:d} argument:".format(i))
            print("{:d}: {:s}".format(i, argv[i]))
        else:
            j = 1
            while j <= i:
                print("{:d}: {:s}".format(j, argv[j]))
                j += 1


if __name__ == "__main__":
    import sys
    Argv(sys.argv)

