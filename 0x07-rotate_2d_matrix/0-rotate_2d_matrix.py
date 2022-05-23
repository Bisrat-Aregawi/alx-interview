#!/usr/bin/env python3
"""Module defines `rotate_2d_matrix` function"""
from typing import Any, List


def rotate_2d_matrix(matrix: List[List[Any]]) -> None:
    """In-place rotate a 2d square matrix 90 deg CW

    Args:
        matrix: list representation of a 2d square matrix

    Returns:
        None
    """
    order = len(matrix)
    for i in range(order):
        for j in range(i, order):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp

    for row in matrix:
        row.reverse()
