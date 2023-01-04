#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

digit = abs(number) % 10
the_string = ""

if number < 0:
    digit = -digit
the_string = f"Last digit of {number} is {digit} and"
if digit > 5:
    print(f"{the_string} is greater than 5")
elif digit == 0:
    print(f"{the_string} is 0")
else:
    print(f"{the_string} is less than 6 and not 0")
