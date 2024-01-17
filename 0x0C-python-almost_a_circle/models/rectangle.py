#!/usr/bin/python3
"""rectangle module containing Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """constructor/Initializing class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instance attributes
        Args: height: int, width : int, x : int, y : int
        Raises: TypeError, ValueError
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def height(self):
        """height getter"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    @property
    def width(self):
        """width getter"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def x(self):
        """x getter"""
        return self.__x
    
    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    
    @property
    def y(self):
        """y getter"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def area(self):
        """returns the area of a rectangle"""
        return self.__height * self.__width
    
    def display(self):
        """prints rectange using # char"""
        [print("") for y in range(self.__y)]

        #res = "#"
        for h in range(self.__height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            # for j in range(self.__width):
            #     print("{}".format(res), end='')
            print(end='\n')
    def update(self, *args):
        if args and len(args) != 0:
            a = 0
            for i in args:
                if a == 0:
                    if i is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = i
                elif a == 1:
                    self.width = i
                elif a == 2:
                    self.height = i
                elif a == 3:
                    self.x = i
                elif a == 4:
                    self.y = i
                a += 1
