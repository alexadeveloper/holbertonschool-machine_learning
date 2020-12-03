#!/usr/bin/env python3
""" function line up """


def add_arrays(arr1, arr2):
    """ function add array"""
    if len(arr1) != len(arr2):
        return None
    else:
        matrix = []
        for index, item in enumerate(arr1):
            matrix.append(item+arr2[index])
        return matrix
