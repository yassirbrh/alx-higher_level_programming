#!/usr/bin/python3


""" write_file - Function """


def write_file(filename="", text=""):
    """ Initialisation of the function write_file """
    with open(filename, "w", encoding="utf-8")as f:
        f.write(text)
    return len(text)
