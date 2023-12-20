#!/usr/bin/python3
"""Representing a class Square"""

class Square:
    """Representing a square"""

    def __init__(self, size=0):
        self.__size = size

    """Retrieving the  size."""
    @property
    def size(self):
        return self.__size

    """Sets the size to val"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")

        self.__size = value

    """Returns square area"""
    def area(self):
        result = self.__size * self.__size
        return result

    """Prints a square with # char"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()