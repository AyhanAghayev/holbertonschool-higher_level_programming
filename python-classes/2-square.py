#!/usr/bin/python3
"""gay program"""


class Square():
    """class"""
    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError
            self.__size = size
        except TypeError:
            print("size must be an integer")
