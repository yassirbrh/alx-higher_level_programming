#!/usr/bin/python3
def magic_string():
    magic_string.loop = getattr(magic_string, 'loop', 0) + 1
    return "Best School, " * (magic_string.loop - 1) + "Best School"
