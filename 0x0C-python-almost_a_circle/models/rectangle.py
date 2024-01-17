#!/usr/bin/python3
"""import Base class from base file"""
from base import Base


class Rectangle(Base):

    """constructor/Initializing class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """instance attributes
        Args: height: int, width : int, x : int, y : int
        Raises: TypeError, ValueError
        """
        """inherit id from base class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    
    """height getter"""
    @property
    def height(self):
        return self.__height
    
    """height setter"""
    @height.setter
    def height(self, value):
        self.__height = value
    
    """width getter"""
    @property
    def width(self):
        return self.__width
    
    """width setter"""
    @width.setter
    def width(self, value):
        self.__width = value
    
    """x getter"""
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value
    
    """y getter"""
    @property
    def y(self):
        return self.__y
    
    """y setter"""
    @y.setter
    def y(self, value):
        self.__y = value

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
