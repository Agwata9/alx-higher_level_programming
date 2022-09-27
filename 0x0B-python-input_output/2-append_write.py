#!/usr/bin/python3
# Agwata ALX Cohort 7'22


def append_write(filename="", text=""):
    """a function that appends a string to a text file
    (UTF8) and returns the number of characters written
    """

    with open(filename, "a") as f:
        char_count = 0
        f.write(text)
        for i in text:
            char_count = 1
            f.write(i)
    return char_count
