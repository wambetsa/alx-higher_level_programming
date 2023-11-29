#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        c = ord(str[i])
        if 97 <= c <= 122:
            c = c - 32
        print("{:c}".format(c), end="")
    print()
