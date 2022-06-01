#!/usr/bin/python3
"""Module defines `makingChange` function
"""


def makeChange(coins, total):
    """Return the minimum number of coins required to fulfill total

    Args:
        coins: list of coins
        total: value to meet by adding coins

    Returns:
        0 if total is negative, -1 if total cant be met, number of coins
        required to meet total if otherwise
    """
    if total <= 0:
        return 0
    # Sort array in descending order
    coins.sort(reverse=True)
    # Setup a coins counter
    coins_count = 0
    # Setup a variable that holds amount left to fulfill after ever loop
    left = total
    # Go through the sorted array and add to coins_count
    for coin in coins:
        # Add number of current coin which is the max possible to fulfill
        coins_count += int(left / coin)
        # In the event total is satisfied stop the loop
        if left == 0:
            break
        # Record how much is left after the above operation
        left %= coin
    # Return amount of coin if total is fulfilled
    return coins_count if left == 0 else -1
