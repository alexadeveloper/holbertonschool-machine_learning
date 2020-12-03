#!/usr/bin/env python3
""" function matrix shape """


def matrix_shape(matrix):
    """ matrix shape function"""
    rows = [len(matrix)]
    for arr in matrix:
        if type(matrix[0]) == list:
            rows.append(len(matrix[0]))
            matrix = matrix[0]
    return rows
