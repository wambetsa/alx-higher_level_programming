#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    result = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            result += 1
        except IndexError:
            pass
    print()            
    return result
