#!/usr/bin/python3
def uppercase(str):
    end_string = ""
    start = 0
    if (len(str) == 0):
        start = -1
    for i in range(start, len(str)):
        if i == -1:
            char = ""
        else:
            char = str[i]
        if i == len(str) - 1:
            end_string = "\n"
        if char != "" and ord(char) > 96 and ord(char) < 123:
            print("{:c}".format(ord(char) - 32), end=end_string)
        else:
            print("{}".format(char), end=end_string)
