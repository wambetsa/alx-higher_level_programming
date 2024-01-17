#!/usr/bin/python3
from models.rectangle import Rectangle


if __name__ == "__main__":
    try:
        r = Rectangle(10, 3)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    
    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(3, 5)
        r.y = -9
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(3,4,6,-4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))