#!/usr/bin/env python3
""" exponential """


class Exponential:
    """ exponential"""
    e = 2.7182818285

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

    def pdf(self, x):
        """pdf"""
        if x < 0:
            return 0
        result = self.lambtha * (Exponential.e ** (self.lambtha * (-1) * x))
        return result
