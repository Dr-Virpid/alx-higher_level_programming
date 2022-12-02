#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = len(argv) - 1
    if args == 1:
        print("{0} argument:\n{0}: {1}".format(args, argv[1]))
    elif args == 0:
        print("{} arguments".format(args))
    else:
        print("{} arguments:".format(args))
    if args > 1:
        for i in range(1, args + 1):
            print("{}: {}".format(i, argv[i]))
