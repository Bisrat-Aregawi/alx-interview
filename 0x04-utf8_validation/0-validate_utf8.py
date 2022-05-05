#!/usr/bin/python3
""" Module defines `validUTF8` function
"""


def validUTF8(data):
    """ Validate whether data set represents valid UTF-8 encoding

    Args:
        data: a list of integers representing bytes in UTF-8

    Returns:
        True if data set holds valid UTF-8 envoding, False otherwise
    """
    validation_table = {
            "0": 0,
            "110": 1,
            "1110": 2,
            "11110": 3,
            }
    left = -1
    for num in data:
        done = False
        bin = bin_str(num)
        if len(bin) == 8:
            if left == 0 or data[0] == num:
                for key in validation_table.keys():
                    if bin_str(num)[:len(key)] == key:
                        left = validation_table[key]
                        done = True
            if done:
                continue

            if len(bin) == 8 and bin[0:2] == "10":
                left -= 1
            else:
                return False
        return False
    return True


def bin_str(num):
    """ Return binary as a string of passed number
    """
    binry = ""

    while num:
        binry += str(num % 2)
        num = int(num / 2)
    if len(binry) < 8:
        binry += '0'*(8 - len(binry))

    return binry[::-1]
