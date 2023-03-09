#!/usr/bin/python3
import random
numb = random.randint(-10, 10)
if numb > 0:
    print("{:d} is positive".format(numb))
elif numb == 0:
    print("{:d} is zero".format(numb))
else:
    print("{:d} is negative".format(numb))
