#!/usr/bin/python3
"""Representing a class Square"""

class Square:
    """Representing a square."""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Retrieving the  size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size to a value."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns square area."""
        res = self.__size * self.__size
        return res