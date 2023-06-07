#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    for i in range(0, len(str)):
        if i != n:
            string += str[i]
    return string
