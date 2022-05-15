#!/usr/bin/python3
"""Module defines `minOperations` function"""


def minOperations(n: int) -> int:
    """Determine minimum number of operations

    For a text editor that supports only `copy all` and
    `paste`, minOperations will determine the minimum
    number of operations (combination of `copy all` & `paste`)
    to get `n` number of characters displayed.
    Args:
        n: Number of characters required

    Returns:
        Ops count, 0 if impossible
    """
    next, prev, ops = 1, 1, 0
    while next < n:
        if n % next != 0:
            next += prev
            ops += 1
        else:
            prev = next
            next *= 2
            ops += 2
    if next == n:
        return ops
    return 0
