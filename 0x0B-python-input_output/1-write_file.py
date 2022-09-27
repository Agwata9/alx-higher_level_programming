#!/usr/bin/python3
# Agwata ALX Cohort 7'22


def read_filewrite_file(filename="", text=""):
    """a function that writes a string to a text file
    (UTF8) and returns the number of characters written
    """

    with open(filename, "w") as f:
        char_count = 0
        f.write(text)
        for i in range(len(text)):
            char_count = 1
    return char_count
