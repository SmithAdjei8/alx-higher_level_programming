#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            numb = 32
        else:
            numb = 0
        print("{:c}".format(ord(str[i]) - numb), end='')
    print()
