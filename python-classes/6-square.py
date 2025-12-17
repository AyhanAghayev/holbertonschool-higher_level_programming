#!/usr/bin/python3
"""This module defines a square class with a private attribute size"""


class Square():
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if (not isinstance(position, tuple) or
            len(position) != 2 or
            not all(isinstance(num, int) for num in position) or
            not all(num > 0 for num in position)):
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
