#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
a class Square that defines a square by: (based on 4-square.py).
"""


class Square:

    """
    a class Square that defines a square by: (based on 3-square.py).
    """

    def __init__(self, size=0):

        """
        Private instance attribute: size Instantiation with size.
        """

        self.size = size

    @property
    def size(self):

        """
        Private instance attribute: size Instantiation with size.
        """

        return self.__size

    @size.setter
    def size(self, value):
        
        """
        Private instance attribute: size Instantiation with size.
        """

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        """
        Private instance attribute: size Instantiation with size.
        """

        a = self.__size * self.__size
        return a

    def my_print(self):

        """
        Private instance attribute: size Instantiation with size.
        """

        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
