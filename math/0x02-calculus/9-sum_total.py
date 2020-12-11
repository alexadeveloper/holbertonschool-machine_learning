#!/usr/bin/env python3
""" function sum total """


def summation_i_squared(n):
    """ function summation """
    i = 1
    suma = 0
    while(i <= n):
        suma = suma + (i * i)
        i = i + 1
    return suma
