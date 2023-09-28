#!/usr/bin/env python3
"""
    Finds the peak in a list of integers.
"""


def find_peak(list_of_integers):
    if list_of_integers is None or list_of_integers == []:
        return None
    peak = None
    length = len(list_of_integers)
    for i in range(length):
        if i == 0:
            peak = list_of_integers[0]
            continue
        if i == length - 1:
            if peak < list_of_integers[i]:
                return list_of_integers[i]
        else:
            prev = list_of_integers[i - 1]
            num = list_of_integers[i]
            after = list_of_integers[i + 1]
            if after < num and num > prev:
                peak = num
    return peak
