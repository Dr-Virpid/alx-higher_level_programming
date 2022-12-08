#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    dict_list = sorted(a_dictionary.items())
    for item in dict_list:
        print(item[0], item[1])
