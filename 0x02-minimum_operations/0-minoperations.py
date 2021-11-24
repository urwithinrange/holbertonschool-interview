#!/usr/bin/python3
import math
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
    nPaste = 1
    nCount = 0

    if n < 2:
        return 0
    while nPaste < n:
        if (n % nPaste == 0):
            nCopy = nPaste
            nCount += 1
        nPaste += nCopy
        nCount += 1
    return nCount

    # # attempt using factorization 
    # count = 0
    # total = 0
    # for t in range(2, int(n)):
    #     if (n % t == 0):
    #         total = t
    #         count += 1
    #     t += total
    #     count += 1
    # return int(count)

    # #worked for most cases just not all edge cases
    # if n < 2:  # This is the case when n is 0 or 1
    #     return 0
    # elif n % 2 == 0: # This is the case when n is a factor of 2
    #     return 2 + minOperations(n / 2)
    # elif n % 3 == 0: # This is the case when n is a factor of 3
    #     return 3 + minOperations(n / 3)
    # elif n % 5 == 0: # This is the case when n is a factor of 5
    #     return 5 + minOperations(n / 5)
    # elif
    # else:  # This is the case when n is prime
    #     return int(n)
    #    # return 1 + minOperations(n - 1)
