#!/usr/bin/python3
"""Defining pascal_triangle"""


def pascal_triangle(n):
    """pascal triangle representation"""
    if n <= 0:
        return []
    triangles = [[1]]
    while len(triangles) != n:
        tr = triangles[-1]
        tmp = [1]
        for i in range(len(tr) - 1):
            tmp.append(tr[i] + tr[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles