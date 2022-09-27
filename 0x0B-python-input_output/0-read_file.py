#!/usr/bin/python3

"""
a function that reads a text file (UTF8)
"""


def read_file(filename=""):
    """ Read a UTF8 text file and
        print it to stdout.
        param: filename - the file to open and read.
    """
    with open(filename, "r") as f:
        text = f.read()
        for line in text:
            print(line, end="")
