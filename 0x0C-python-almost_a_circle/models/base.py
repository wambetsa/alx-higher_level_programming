#!/usr/bin/python3
"""Base class"""


class Base:
    """private class attribute"""
    __nb_objects = 0

    """constructor/instantiating object"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

#usage of above class
if __name__ == "__main__":
    #print output
    b1 = Base()
    b2 = Base()
    b3 = Base(20)
    b4 = Base()
    b5 = Base()
    
    print(b1.id)
    print(b2.id)
    print(b3.id)
    print(b4.id)
    print(b5.id)