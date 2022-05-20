#!/usr/bin/python3
"""
Python function given a set of consecutive integers
starting from 1 up to and including n take turns choosing
a prime number from the set and removing that number and its
multiples from the set. Returns the player with the most wins
or none for a tie.
"""


def isPrime(num):
        """
        Return: a list of primes in range of num
        """
        primes = []
        Pfilter = [True] * (num + 1)
        for i in range(2, num + 1):
                if Pfilter[i]:
                        primes.append(i)
                        for j in range(i * i, num + 1, i):
                                Pfilter[j] = False
        return primes


def isWinner(x, nums):
        """where x is the number of rounds and nums is an array of n
        Return: name of the player that won the most rounds
        If the winner cannot be determined, return None
        You can assume n and x will not be larger than 10000
        You cannot import any packages in this task
        players are Maria Player 1 and Ben player 2
        """

        if x is None or nums is None or x == 0 or nums == []:
                return None

        P1Score = 0  # maria
        P2Score = 0  # ben

        for i in range(x):
                primes = isPrime(nums[i])
                if len(primes) % 2 != 0:  # if the number of primes is odd
                        P1Score += 1
                else:  # if the number of primes is even
                        P2Score += 1
        if P1Score > P2Score:
                return "Maria"
        elif P2Score > P1Score:
                return "Ben"
        else:
                return None
