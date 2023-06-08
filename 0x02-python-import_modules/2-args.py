#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    index = 0
    if len(argv) == 1:
        print("0 arguments.")
    else:
        if len(argv) == 2:
            print("1 argument:")
        else:
            print("{:d} arguments:".format(len(argv) - 1))
        for arg in argv:
            if index != 0:
                print("{:d}: {}".format(index, arg))
            index += 1
