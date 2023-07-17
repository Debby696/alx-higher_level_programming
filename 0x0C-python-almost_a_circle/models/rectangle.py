#!/usr/bin/python3
""" This is a class rectangle that inherits from base"""

from base import Base


class Rectangle(Base):
    """This depicts a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Objects attributes are initialized"""
        Base.__init__(self, id=None)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """Getter function"""
    @property
    def width(self):
        """This gets the value for the width"""
        return self.__width

    @property
    def height(self):
        """This gets the value for the  height"""
        return self.__height

    @property
    def x(self):
        """This is used to get the value for x"""
        return self.__x

    @property
    def y(self):
        """This is used to get the value for y"""
        return self.__y

    """ setter functions"""
    @width.setter
    def width(self, input):
        """This sets the value for width"""
        if (input is not int):
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

    @height.setter
    def height(self, input):
        """This sets the value for height"""
        if (input is not int):
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

    @x.setter
    def x(self, input):
        """This sets the value for x"""
        if (input is not int):
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

    @y.setter
    def y(self, input):
        """This sets the value for y"""
        if (input is not int):
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

    @property
    def area(self):
        """This defines the area of the rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """This displays the Rectangle instance with the character #"""
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """This gives a format to represent the string of the class"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - 
        {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """This assigns an argument to each attribute"""

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1








     def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""

        obj_dictionary = {'id': self.id, 'width': self.__width,
                          'height': self.__height, 'x': self.__x,
                          'y': self.__y}

        return obj_dictionary
