#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    i = 0
    for num in my_list:
        if i == idx:
            my_list[i] = element
        i += 1
    return my_list
