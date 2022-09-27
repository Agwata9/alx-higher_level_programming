#!/usr/bin/python3

"""
a function that reads a text file (UTF8)
"""

def read_file(filename=""):
    """a function that reads a text file (UTF8)
    and prints it to stdout
    """

    with open(filename, "r") as f:
        text = f.read()
        for line in text:
            print(line, end="")
