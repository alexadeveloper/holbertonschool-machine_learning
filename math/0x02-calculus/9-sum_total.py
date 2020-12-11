#!/usr/bin/env python3
""" function sum total """


def summation_i_squared(n):
    """ function summation """
    if n <= 0:
        return None
    if type(n) != int:
        return None
    return int((n * (1 + n) * (1 + 2 * n)) / 6)
