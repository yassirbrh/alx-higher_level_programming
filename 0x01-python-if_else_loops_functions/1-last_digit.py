#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = -number
    lastDigit = number % 10
    number = -number
    lastDigit = -lastDigit
else:
    lastDigit = number % 10
print(f"Last digit of {number}", end=" ")
if lastDigit == 0:
    print("is {} and is 0".format(lastDigit))
elif lastDigit > 5:
    print("is {} and is greater than 5".format(lastDigit))
elif lastDigit < 6:
    print("is {} and is less than 6 and not 0".format(lastDigit))
