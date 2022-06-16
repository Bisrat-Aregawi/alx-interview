#!/usr/bin/python3
"""Module defines `isWinner` function
"""


def isWinner(x, nums):
    """Return name of the player that won most rounds

    Args:
        x: length of `nums` list
        nums: list of numbers

    Returns:
        `Maria` if maria wins, `Ben` otherwise
    """
    scores = [0, 0]
    for idx in range(x):
        if idx <= len(nums) - 1:
            if nums[idx] < 2:
                scores[1] = scores[1] + 1
                continue
            num_range = [x for x in range(2, nums[idx] + 1)]
            i = 0
            while True:
                if isPrime(num_range[0]) is True:
                    j = 0
                    modulator = num_range[0]
                    while j < len(num_range):
                        if (num_range[j] % modulator) == 0:
                            num_range.remove(num_range[j])
                        else:
                            j = j + 1
                if num_range == []:
                    scores[i % 2] = scores[i % 2] + 1
                    break
                i = i + 1
    if (scores[0] > scores[1]):
        return 'Maria'
    else:
        return 'Ben'


def isPrime(num):
    """Check if number is prime or not

    Args:
        nums: list of numbers

    Returns:
        `True` if prime, `False` otherwise
    """
    if num < 2:
        return False
    for x in range(2, int(num / 2)):
        if num % x == 0:
            return False
    return True
