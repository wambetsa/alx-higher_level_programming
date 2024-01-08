#!/usr/bin/python3
"""
    Prototype: def say_my_name(first_name, last_name=""):
    first_name and last_name must be strings 
    else raise a TypeError exception with the message
    first_name must be a string or last_name must be a string
"""

def say_my_name(first_name, last_name=""):
    """
        print my first and last name
    """
    str_error = "first_name must be a string or last_name must be a string"
    if type(first_name) is not str or type(last_name) is not str:
        raise TypeError(str_error)
    print("My name is", first_name, last_name)