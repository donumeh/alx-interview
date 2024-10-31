#!/usr/bin/env python3

"""
Validate UTF-8 character sets
"""


def validUTF8(data):
    """
    validUTF8: function that validates the data set

    data: type(List): Checks each elems in the sets to validate if its at least 8 bits
    """
    min_printable = 32
    max_printable = 127
    for char in data:
        if char < min_printable or char > max_printable:
            # print(char)
            return False

    return True
