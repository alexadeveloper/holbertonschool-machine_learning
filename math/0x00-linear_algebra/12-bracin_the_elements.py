#!/usr/bin/env python3
""" bracin the elements """


def np_elementwise(mat1, mat2):
    """ performs add, sub """
    suma = mat1 + mat2
    rest = mat1 - mat2
    mult = mat1 * mat2
    div = mat1 / mat2
    return suma, rest, mult, div
