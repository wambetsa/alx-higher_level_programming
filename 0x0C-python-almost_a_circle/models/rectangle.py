#!/usr/bin/python3
"""import Base class"""
from models.base import Base


"""Rectangle class"""
class Rectangle(Base):
    """init constructor"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """inherit attributes from Base class"""
        """Args: width, height, x, y, id
        Raises: TypeError, ValueError, TypeError, ValueError
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    """width getter"""
    @property
    def width(self):
        return self.__width
    
    """width setter"""
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise  ValueError("width must be > 0")
        self.__width = value

    """height getter"""
    @property
    def height(self):
        return self.__height
    
    """height setter"""
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    """x getter"""
    @property
    def x(self):
        return self.__x
    
    """x setter"""
    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value
    
    """y getter"""
    @property
    def y(self):
        return  self.__y
    
    """y setter"""
    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value
        
