#!/usr/bin/python3
"""
    a function that returns True if the object is an instance 
    of, or if the object is an instance of a class that 
    inherited from, the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """ true if obj inherits from a_class """
    return issubclass(type(obj), a_class) and (type(obj) != a_class)