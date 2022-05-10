#!/usr/bin/python3
"""
Function that returns the perimeter of the island in a grid
"""


def island_perimeter(grid):
        """
        Function that checks through the grid and determines
        how many cells are touched by water. The first and last
        rows of the grid should be considered borders,
        and any cell touching them should count as a perimeter.
        The first and last columns of the grid should be considered borders,
        and any cell touching them should count as a perimeter.
        """
        count = 0
        for row in range(len(grid)):  # rows
                for col in range(len(grid[row])):  # columns
                        if grid[row][col] == 1:  # if the cell is land
                                # if first row or cell above
                                if row == 0 or grid[row - 1][col] == 0:
                                        count += 1
                                # if last row or cell to the bottom
                                if row == len(grid) - 1 or \
                                        grid[row + 1][col] == 0:
                                        count += 1
                                # if first column or cell to the left
                                if col == 0 or grid[row][col - 1] == 0:
                                        count += 1
                                # if last column or cell to the right
                                if col == len(grid[row]) - 1 or \
                                        grid[row][col + 1] == 0:
                                        count += 1
        return count
