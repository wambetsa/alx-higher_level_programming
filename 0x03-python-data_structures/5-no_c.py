#!/usr/bin/python3

def no_c(my_string):
    n_string = ""
    for c in my_string:
        if c not in 'cC':
            n_string += c
    return n_string
