#!/usr/bin/python3
"""
Python function given a set of consecutive integers
starting from 1 up to and including n take turns choosing
a prime number from the set and removing that number and its 
multiples from the set. Returns the player with the most wins 
or none for a tie.
"""

def isWinner(x, nums):
	"""where x is the number of rounds and nums is an array of n
	Return: name of the player that won the most rounds
	If the winner cannot be determined, return None
	You can assume n and x will not be larger than 10000
	You cannot import any packages in this task
	players are Maria Player 1 and Ben player 2
	"""
	P1Score = 0
	P2Score = 0
	nums = sorted(nums)
	
	while x > 0:
		for i in range(len(nums)):
			
		if nums[0] % 2 == 0:
			P1Score += 1
			nums.pop(0)
		else:
			P2Score += 1
			nums.pop(0)
		x -= 1
		# for num in range(len(nums)):
		# 	if num <= 1:

		# 	if num % 2 == 0:
		# 		P1Score += 1
		# 		nums.remove(num)
		# 	elif num % 2 == 1:
		# 		P2Score += 1
		# 		nums.remove(num)
		# if nums[0] % 2 == 0
