#!/usr/bin/python3
"""
    class BaseGeometry (based on 6-base_geometry.py).

    Public instance method: def area(self): raises an Exception 
    with the message area() is not implemented Public instance method:
    def integer_validator(self, name, value):
        that validates value:
        you can assume name is always a string
        if value is not an integer: raise a TypeError
        exception, with the message <name> must be an integer
        if value is less or equal to 0: raise a ValueError
        exception with the message <name> must be greater
        than 0
"""


class BaseGeometry:
    """ empty BaseGeometry class """

    def area(self):
        """ raise exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value is an int """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))