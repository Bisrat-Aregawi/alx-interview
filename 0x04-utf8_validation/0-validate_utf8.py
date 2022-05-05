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
    idx1 = 0
    while idx1 < len(data):
        bytes = bytes_count(data[idx1])
        if bytes is not None:
            idx2 = 1
            while idx2 < bytes:
                if idx1 + idx2 >= len(data) or data[idx1 + idx2] & 192 != 128:
                    return False
                idx2 += 1
            idx1 += bytes
    return True


def bytes_count(num):
    """ Return number of bytes represented by number
    """
    if num >= 255:
        return None
    if num & 128 == 0:
        return 1
    elif num & 224 == 192:
        return 2
    elif num & 240 == 224:
        return 3
    elif num & 248 == 240:
        return 4
    else:
        return None
