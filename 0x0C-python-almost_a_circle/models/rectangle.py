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
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    """height getter"""
    @property
    def height(self):
        return self.__height
    
    """height setter"""
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    """width getter"""
    @property
    def width(self):
        return self.__width
    
    """width setter"""
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    """x getter"""
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    
    """y getter"""
    @property
    def y(self):
        return self.__y
    
    """y setter"""
    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)