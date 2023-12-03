#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        n_list = my_list.copy()
        n_list.reverse()
        for i in n_list:
            print("{:d}".format(i))
