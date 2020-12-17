#!/usr/bin/env python3
""" exponential """


class Exponential:
    """ exponential"""
    def __init__(self, data=None, lambtha=1.):
        """ function lambtha"""
        self.lambtha = float(lambtha)
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
        else:
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            isList = type(data)
            if isList != list:
                raise TypeError("data must be a list")
            self.lambtha = float(sum(data) / len(data))
