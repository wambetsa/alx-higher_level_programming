#!/usr/bin/python3
""" empty Rectangle class that defines a rectangle
"""


class Rectangle:
    """ class Rectangle"""
    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width of rectangle
        """
        return self.__width

    @property
    def height(self):
        """height of rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ width of rectangle setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height of rectangle setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value