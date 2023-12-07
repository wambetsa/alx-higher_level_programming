#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = my_list[:]
    n_list = [x if x != search else replace for x in my_list]
    return(n_list)
