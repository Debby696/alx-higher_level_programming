#!/usr/bin/python3
def display(width, height):
    """This displays the Rectangle instance with the character #"""
    """for x in range(self.__height):
        print(self.__width* "#")
        display (2,5)"""

         for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()
