#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    first_sum = 0
    second_sum = 0
    sum_list = [first_sum, second_sum]
    for i in range(2):
        try:
            sum_list[i] += tuple_a[i]
        except IndexError:
            sum_list[i] += 0

        try:
            sum_list[i] += tuple_b[i]
        except IndexError:
            sum_list[i] += 0
    return (first_sum, second_sum)
