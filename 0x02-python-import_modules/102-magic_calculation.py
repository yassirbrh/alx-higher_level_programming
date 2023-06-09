#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
    else:
        for i in range(89):
            c = add(c, i)

__import__("dis").dis(magic_calculation)
