#!/usr/bin/python3
def magic_string():
    magic_string.loop = getattr(magic_string, 'loop', 0) + 1
    return "BestSchool, " * (magic_string.loop - 1) + "BestSchool"
