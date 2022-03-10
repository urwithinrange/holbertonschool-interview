#!/usr/bin/python3
"""
0x00-rain.py
This module contains the function rain().
"""
def rain(walls):
        """
        This function takes a list of integers 
        and returns an int equal the volume of water
        trapped between walls of various heights.
        """
        max_height = max(walls)
        L_wall_height = 0
        R_wall_height = 0
        left_index = 0
        right_index = (len(walls) - 1)
        water = 0

        if not walls:
                return (0)

        for i in range(len(walls)): #left approach to wall of max height
                if walls[i] != 0 and walls[left_index] <= walls[i]:
                        L_wall_height = walls[i] #the amount of water that can be held
                        left_index = i #wall index height > 0
                elif walls[i] == 0 and L_wall_height > 0:
                        water += L_wall_height #Add water if an amount is present
                if walls[i] == max_height:
                        left_index = i #Stores the index of the wall of max height
                        break
        for r in range(len(walls) - 1, -1, -1): #right approach to left wall index
                if walls[r] != 0 and walls[right_index] <= walls[r]:
                        R_wall_height = walls[r] #the amount of water that can be held
                        right_index = r #wall index height > 0
                elif walls[r] == 0 and R_wall_height > 0:
                        water += R_wall_height #Add water if an amount is present
                if right_index == left_index:
                        break #break once the right index is equal to the left index
        return (water)
