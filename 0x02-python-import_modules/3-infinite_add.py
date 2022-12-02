#!/usr/bin/python3
from sys import argv
def add(args):
    sums = 0
    for i in args[1:]:
        sums += int(i)
    return sums

if __name__ == "__main__":
    print(add(argv))
