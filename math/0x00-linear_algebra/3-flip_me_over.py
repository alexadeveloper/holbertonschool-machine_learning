#!/usr/bin/env python3
""" function matrix transpose """


def matrix_transpose(matrix):
    """ matrix transpose fuction """
    newMatrix = list(map(list, zip(*matrix)))
    return newMatrix
