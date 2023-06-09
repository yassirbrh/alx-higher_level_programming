#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    new_list = []
    i = 0
    for num in my_list:
        if i == idx:
            new_list.append(element)
        else:
            new_list.append(my_list[i])
        i += 1
    return new_list
