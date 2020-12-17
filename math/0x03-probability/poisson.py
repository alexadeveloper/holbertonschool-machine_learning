#!/usr/bin/env python3
""" Function poison """


class Poisson:
    """class poisson"""
    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        """ Function poisson"""

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

    def pmf(self, k):
        """ function PMF """
        if k <= 0:
            return 0
        if type(k) != int:
            k = int(k)
        f = 1
        for i in range(1, k + 1):
            f *= i
        result = ((self.lambtha ** k) * Poisson.e ** (self.lambtha * (-1))) / f
        return result

    def cdf(self, k):
        """ function cdf """
        if k < 0:
            return 0
        if type(k) != int:
            k = int(k)
        f = [1]
        for j in range(1, k + 1):
            f.append(f[j - 1] * j)
        rescdf = (Poisson.e ** (self.lambtha * (-1))) * sum([
                (self.lambtha ** j) / f[j] for j in range(0, k + 1)])
        return rescdf
