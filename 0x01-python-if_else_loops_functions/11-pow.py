#!/usr/bin/python3
def pow(a, b):
    expo = b
    if b < 0:
        expo = -b
    elif b == 0:
        return 1
    result = a
    for i in range(expo - 1):
        result *= a
    if b < 0:
        return 1 / result
    else:
        return result
