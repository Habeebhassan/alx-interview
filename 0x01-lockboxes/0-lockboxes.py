#!/usr/bin/python3
"""
Method to determine if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Check if boxes can be unlocked
    """
    for key in range(1, len(boxes) - 1):
        ct = False
        for idx in range(len(boxes)):
            ct = (key in boxes[idx] and key != idx)
            if ct:
                break
        if ct is False:
            return ct
    return True
