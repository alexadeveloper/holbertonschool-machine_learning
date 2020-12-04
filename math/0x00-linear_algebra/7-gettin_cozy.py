#!/usr/bin/env python3
""" gettin cozy """


def cat_matrices2D(mat1, mat2, axis=0):
    """concatenates two matrices"""
    if axis == 1 and (len(mat1) == len(mat2)):
        return [mat1[index]+mat2[index] for index, item in enumerate(mat2)]
    if axis == 0:
        row1 = [arr[:] for arr in mat1]
        row2 = [arr2[:] for arr2 in mat2]
        return row1 + row2
