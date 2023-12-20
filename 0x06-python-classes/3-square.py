#!/usr/bin/python3
"""Respresenting class Square"""

class Square:
    """Representing a square"""

    def __init__(self, size=0):
        """Initializing private"""
        self.__size = size
        if size is not int(size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")

    def area(self):
        """Returns square area."""
        res = self.__size * self.__size
        return res