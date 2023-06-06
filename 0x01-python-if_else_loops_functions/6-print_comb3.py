#!/usr/bin/python3
start = 1
for i in range(10):
    for j in range(start, 10):
        if i != j:
            if i == 8 and j == 9:
                print("{}{}".format(i, j))
            else:
                print("{}{},".format(i, j), end=" ")
    start += 1
