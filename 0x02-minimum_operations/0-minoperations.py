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

    if n < 2:  # This is the case when n is 0 or 1
        return 0
    elif n % 2 == 0: # This is the case when n is a factor of 2
        return 2 + minOperations(n / 2)
    elif n % 3 == 0: # This is the case when n is a factor of 3
        return 3 + minOperations(n / 3)
    else:  # This is the case when n is prime
        return int(n)
