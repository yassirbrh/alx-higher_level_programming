#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum_tuple = 0
    sum_weight = 0
    for tup in my_list:
        sum_tuple += tup[0] * tup[1]
        sum_weight += tup[1]
    return sum_tuple / sum_weight
