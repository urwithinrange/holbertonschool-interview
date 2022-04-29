#!/usr/bin/python3
""" Function that returns the minimum number of coins needed to make change """

def makeChange(coins, total):
        """
        Function that returns the minimum number of coins needed to make change
        """
        count = 0
        i = 0
        coin = len(coins)
        if coin == 0 and total != 0:
                return -1
        coins.sort(reverse=True)
        while total > 0:
                if coins[i] <= total:
                        total -= coins[i]
                        count += 1
                else:
                        i += 1
                        if i >= coin:
                                return -1
        return count
