#!/usr/bin/python3
class Square:
    """a class Square that defines a square by: (based on 0-square.py)."""
    def __init__(self, size=0):
        """Private instance attribute: size Instantiation with size."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Public instance method:"""
        area = self.__size*self.__size
        return area
