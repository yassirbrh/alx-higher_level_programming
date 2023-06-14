#!/usr/bin/python3
def simple_delete(a_dictionary, keys=""):
    if a_dictionary.get(keys) != None:
        del(a_dictionary[keys])
    return a_dictionary
