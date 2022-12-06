#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    div_2 = lambda num: num % 2 == 0
    new_list = [div_2(num) for num in my_list]
    return new_list
