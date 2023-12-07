#!/usr/bin/python3
def uniq_add(my_list=[]):
    summation = 0
    n_list = sorted(my_list)
    for i in range(len(n_list)):
        if i == 0 or n_list[i] != n_list[i - 1]:
            summation += n_list[i]
    return(summation)
