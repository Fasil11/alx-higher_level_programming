#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

digit = abs(number) % 10

if number < 0:
    digit = -digit

    print(f"the last digit of {number} is {digit} and")

if digit > 5:
    print("is greater than 5")
elif digit == 0:
    print("is 0")
else:
    print("is less than 6 and not 0")
