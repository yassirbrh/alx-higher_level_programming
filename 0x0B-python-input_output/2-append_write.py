#!/usr/bin/python3


""" append_write - Function """


def append_write(filename="", text=""):
    """ Initialisation of the function append_write """
    with open(filename, "a", encoding="utf-8")as f:
        f.write(text)
    return len(text)
