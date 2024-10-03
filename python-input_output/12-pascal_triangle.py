#!/usr/bin/python3
"""Module for Pascal's triangle"""


def pascal_triangle(n):
    """Function list of lists of integers to represent
    the Pascal's triangle of n"""
    if n <= 0:
        return []
    triangle = []
    for num in range(0, n):
        res = [int(x) for x in str(pow(11, num))]
        triangle.append(res)
    return triangle
