#!/usr/bin/python3

def canUnlockAll(boxes):
    keysSet = {0}
    recurse(0, boxes, keysSet)
    return list(keysSet) == list(range(len(boxes)))

def recurse(idx, boxes, keysSet):
    for key in boxes[idx]:
        if key not in keysSet and key < len(boxes):
            keysSet.add(key)
            recurse(key, boxes, keysSet)
    return None
