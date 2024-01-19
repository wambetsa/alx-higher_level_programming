#!/usr/bin/python3

"""Definition of Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Representation"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square attributes
        Args:
            size (int): new Square size
            x (int): x coordinate
            y (int): y coordinate
            id (int): identity
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Square update
        Args:
            *args (int):
                - 1st arg reps id
                - 2nd arg reps size
                - 3rd arg reps x
                - 4th arg reps y
            **kwargs (dict): New key/value pairs 
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """return dictionary rep of square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """new str format"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)