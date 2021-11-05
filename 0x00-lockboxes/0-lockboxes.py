#!/usr/bin/python3
"""Method that determines if a box can be opened"""


def canUnlockAll(boxes):
    """Determines if a box can be opened"""
    keyring = [0]
    lastBox = 0
    
    while lastBox < len(keyring):
        lastBox = len(keyring)
        for box in range(len(boxes)):
            if box in keyring:
                for key in boxes[box]:
                    if key < len(boxes) and key not in keyring:
                        keyring.append(key)
    return len(keyring) == len(boxes)
