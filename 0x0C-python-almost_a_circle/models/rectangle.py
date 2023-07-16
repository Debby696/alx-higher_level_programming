#!/usr/bin/python3
""" This is a class rectangle that inherits from base"""

from models.base import Base


class Rectangle(Base):
    """This depicts a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Objects attributes are initialized"""
        Base.__init__(self, id=None)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

