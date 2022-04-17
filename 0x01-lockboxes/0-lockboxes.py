#!/usr/bin/python3
"""Graph data structure traversal"""


def canUnlockAll(boxes):
    """Check if all boxes can be recursively opened

    Function, by the help of helper function `recurse`, checks whether all
    boxes in `boxes` 2D list can be opened by begining with keys found on box
    at index 0.

    Args:
        boxes (list of list): 2D list with elements as boxes containing keys

    Returns: True if created set has all keys, false otherwise
    """
    keysSet = {0}
    recurse(0, boxes, keysSet)
    return list(keysSet) == list(range(len(boxes)))


def recurse(idx, boxes, keysSet):
    """Recurse through boxes and enumerate a set with found keys

    Args:
        idx (number): Position indicator for a box in `boxes`
        boxes (2D list): Original list of boxes
        keysSet (set): Data structure for holding unique keys in

    Returns:
        None
    """
    for key in boxes[idx]:
        if key not in keysSet and key < len(boxes):
            keysSet.add(key)
            recurse(key, boxes, keysSet)
    return None
