#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
    roman['M'] = 1000
    number = 0
    i = 0
    for num in roman_string:
        if i + 1 > len(roman_string) - 1:
            break
        if roman[roman_string[i + 1]] == roman[num]:
            number += roman[num] * 2
        elif roman[roman_string[i + 1]] > roman[num]:
            number += roman[roman_string[i + 1]] - roman[num]
        else:
            number += roman[roman_string[i + 1]] + roman[num]
        i += 1
    for i in range(1, len(roman_string) - 1):
        number -= roman[roman_string[i]]
    if len(roman_string) == 1:
        number += roman[roman_string[0]]
    return number
