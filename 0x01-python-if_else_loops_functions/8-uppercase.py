#!/usr/bin/python3
def uppercase(str):
    end_string = ""
    for i in range(0, len(str)):
        if i == len(str) - 1:
            end_string = "\n"
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            print("{:c}".format(ord(str[i]) - 32), end=end_string)
        else:
            print("{}".format(str[i]), end=end_string)
