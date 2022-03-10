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

        if not walls:
                return (0)

        max_height = max(walls)
        L_wall, R_wall = 0, 0
        L_index, R_index = 0, len(walls) - 1
        water = 0

        for i in range(len(walls)):  # Left approach to wall of max height
                if walls[i] != max_height:
                        L_wall = max(L_wall, walls[i])  # = highest value
                        water += L_wall - walls[i]  # vol less underwater wall
                if walls[i] == max_height:
                        L_index = i  # The index of the wall of max height
                        break
        for r in range(len(walls) - 1, -1, -1):  # Right approach to L index
                if R_index != L_index:
                        R_wall = max(R_wall, walls[r])  # = highest value
                        R_index = r  # Wall index height > 0
                        water += R_wall - walls[r]  # vol less underwater wall
                if R_index == L_index:
                        break  # Break when the R index == L index
        return (water)
