#!/usr/bin/env python3
""" ridin bareback """


def zeros_matrix(rows, cols):
    """ Creates a matrix filled with zeros. """
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)
    return M


def mat_mul(mat1, mat2):
    """ Multiply 2 matrix"""
    rowsA = len(mat1)
    colsA = len(mat1[0])
    rowsB = len(mat2)
    colsB = len(mat2[0])
    if colsA != rowsB:
        return None
    else:
        C = zeros_matrix(rowsA, colsB)
        for i in range(rowsA):
            for j in range(colsB):
                total = 0
                for ii in range(colsA):
                    total += mat1[i][ii] * mat2[ii][j]
                C[i][j] = total
        return C
