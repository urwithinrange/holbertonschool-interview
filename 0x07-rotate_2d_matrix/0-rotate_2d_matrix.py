#!/usr/bin/python3
"""
Rotate a 2D matrix by 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Function that rotates a 2D matrix by 90 degrees clockwise
    """
    new_matrix = list(zip(*matrix[::-1]))
    for x in range(len(new_matrix)):
        for y in range(len(new_matrix[x])):
            matrix[x][y] = new_matrix[x][y]
    return new_matrix
