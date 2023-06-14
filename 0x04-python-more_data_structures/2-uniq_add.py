#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    sum_num = 0
    for num in my_list:
        if num not in new_list:
            sum_num += num
            new_list.append(num)
    return sum_num
