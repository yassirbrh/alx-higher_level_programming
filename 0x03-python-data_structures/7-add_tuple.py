#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_int = [0, 0, 0, 0]
    i = 0
    for num in tuple_a:
        if i == 2:
            break
        list_int[i] = tuple_a[i]
        i += 1
    i = 0
    for num in tuple_b:
        if i + 2 == 4:
            break
        list_int[i + 2] = tuple_b[i]
        i += 1
    new_tuple = (list_int[0] + list_int[2], list_int[1] + list_int[3])
    return new_tuple
