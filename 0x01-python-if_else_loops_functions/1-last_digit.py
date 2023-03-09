#!/usr/bin/python3
import random
numb = random.randint(-10000, 10000)

if numb >= 0:
    l_digit = numb % 10
else:
    l_digit = numb % -10

print("Last digit of {} is {}".format(numb, l_digit), end='')

if l_digit > 5:
    print(" and is greater than 5")
elif l_digit == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
