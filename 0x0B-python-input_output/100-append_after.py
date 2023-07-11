#!/usr/bin/python3
'''
    append_after - Function
'''


def append_after(filename="", search_string="", new_string=""):
    '''
        Function append after search string by new string
    '''
    text = []
    with open(filename, "r") as f:
        for line in f:
            text.append(line)
    new_text = []
    for line in text:
        new_text.append(line)
        if search_string in line:
            new_text.append(new_string)
    with open(filename, "w") as f:
        for line in new_text:
            f.write(line)
