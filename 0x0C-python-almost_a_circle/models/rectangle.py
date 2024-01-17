#!/usr/bin/python3
"""import Base class from models.base"""
from models.base import Base


class Rectangle(Base):

    """constructor/Initializing class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """instance attributes"""
        """inherit id from base class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
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
    