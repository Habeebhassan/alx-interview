#!/usr/bin/python3
"""2D Matrix"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): The n x n matrix to be rotated.

    Returns:
        None: The function modifies the matrix in-place.
    """
    # Step 1: Transpose the matrix (rows become columns)
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            # Swap element (i, j) with element (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

