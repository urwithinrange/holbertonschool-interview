#!/usr/bin/python3
"""
Method that determines the number of operations needed
to copy paste a specific number of times
"""


def minOperations(n):
    """
    Returns the minimum number of
    Copy All and Paste operations needed
    to create (n) "H" characters in a text file
    """
    nCopy = 0
    nPaste = 1  # 1 for the first "H"
    nCount = 0

    if n < 2:  # if n is less than 2, return 0
        return 0

    while nPaste < n:  # nPaste is the number of characters to paste
        if (n % nPaste == 0):  # nCopy will be used here characters to copy
            nCopy = nPaste
            nCount += 1
        nPaste += nCopy
        nCount += 1  # nCount is how many operations are needed
    return nCount
