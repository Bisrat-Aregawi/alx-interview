#!/usr/bin/python3
"""Module Defines function that returns pascal's triangle of height n"""


def pascal_triangle(n):
    """Function constructs list of lists with pascal's triangle coeeficients

    Args:
        n (number): Represents height of triangle

    Returns:
        List of list representing pascal's triangle of height n, [] if n <= 0
    """
    parent = []
    if n > 0:
        previous = []
        for i in range(n):
            current = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    current.append(1)
                elif i > 1:
                    current.append(
                        previous[j - 1] + previous[j]
                    )
            previous = current
            parent.append(current)
    return parent
