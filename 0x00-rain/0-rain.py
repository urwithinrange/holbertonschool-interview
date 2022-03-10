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
        L_wall = 0
        R_wall = 0
        L_index = 0
        R_index = (len(walls) - 1)
        water = 0

        if not walls:
                return (0)

        for i in range(len(walls)):  # Left approach to wall of max height
                if walls[i] != 0 and walls[L_index] <= walls[i]:
                        L_wall = walls[i]
                        L_index = i  # Wall index height > 0
                elif walls[i] == 0 and L_wall > 0:
                        water += L_wall  # Add water if an amount is present
                if walls[i] == max_height:
                        L_index = i  # The index of the wall of max height
                        break
        for r in range(len(walls) - 1, -1, -1):  # Right approach to L index
                if walls[r] != 0 and walls[R_index] <= walls[r]:
                        R_wall = walls[r]
                        R_index = r  # Wall index height > 0
                if walls[r] != 0 and R_wall > walls[r]:  # Underwater wall
                        water += R_wall - walls[r]
                elif walls[r] == 0 and R_wall > 0:
                        water += R_wall  # Add water if an amount is present
                if R_index == L_index:
                        break  # Break when the R index == L index
        return (water)
