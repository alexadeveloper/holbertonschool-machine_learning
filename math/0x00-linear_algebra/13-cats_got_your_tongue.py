#!/usr/bin/env python3
""" bracin the elements """
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """ Concatenate matrix """
    new = np.concatenate((mat1, mat2), axis)
    return new
