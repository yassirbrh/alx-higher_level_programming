#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    i = 0
    new_list = []
    for num in my_list:
        if idx != i:
            new_list.append(my_list[i])
        i += 1
    my_list.clear()
    for num in new_list:
        my_list.append(num)
    return new_list
