#!/usr/bin/python3
"""Module for Pascal's triangle"""


def pascal_triangle(n):
    """Function list of lists of integers to represent
    the Pascal's triangle of n"""
    if n <= 0:
        return []
    if n == 1:
        return [1]
    triangle = [[1], [1, 1]]
    for num in range(2, n):
        last = triangle[num - 1]
        res = [1] + [last[i] + last[i + 1] for i in range(len(last) - 1)] + [1]
        triangle.append(res)
    return triangle
