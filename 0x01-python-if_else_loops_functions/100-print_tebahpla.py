#!/usr/bin/python3
for char in range(122, 96, -1):
    pr_char = char
    if char % 2 == 1:
        pr_char = char - 32
    print("{:c}".format(pr_char), end="")
