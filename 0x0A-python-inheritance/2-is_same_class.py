#!/usr/bin/python3
"""a function that returns True if the object is exactly an instance of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """Functions checks if object is exactly of specified class"""
    return type(obj) is a_class