#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """MyList inherits from list"""
    
    def print_sorted(self):
        """MyList inherits from list Args: self Return: list[]"""
        print(sorted(self))
