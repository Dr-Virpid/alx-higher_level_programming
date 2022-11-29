#!/usr/bin/python3

def uppercase(string):
    for letter in string:
        num_eqv = ord(letter)
        if num_eqv > 96 and num_eqv < 123:
            num_eqv -= 32
        print("{}".format(chr(num_eqv)), end="")
    print()
