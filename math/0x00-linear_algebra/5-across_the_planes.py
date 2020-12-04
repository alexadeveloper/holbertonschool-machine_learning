#!/usr/bin/env python3
""" function across the planes """


def add_matrices2D(mat1, mat2):
    """ add matrices """
    suma = []
    if len(mat1) != len(mat2):
        return None
    else:
        for i in range(len(mat1)):
            if len(mat1[i]) == len(mat2[i]):
                suma1 = [mat1[i][j] + mat2[i][j] for j in range(len(mat1[i]))]
                suma.append(suma1)
            else:
                return None
        return suma
