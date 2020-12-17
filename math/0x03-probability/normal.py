#!/usr/bin/env python3
""" normal """


class Normal:
    """ class normal """

    pi = 3.1415926536
    e = 2.7182818285

    def __init__(self, data=None, mean=0., stddev=1.):
        """" constructor """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            if type(data) != list:
                raise TypeError("data must be a list")
            self.mean = float(sum(data) / len(data))
            self.stddev = ((sum([
                           (data[j] - self.mean) ** 2 for j in
                           range(len(data))])) / len(data)) ** 0.5

    def z_score(self, x):
        """z_score"""
        resz = (x - self.mean) / self.stddev
        return resz

    def x_value(self, z):
        """x_value"""
        resx = z * self.stddev + self.mean
        return resx

    def pdf(self, x):
        """ PDF """
        t = 1 / (self.stddev * ((2 * Normal.pi)) ** 0.5)
        t2 = Normal.e ** (-0.5 * ((x - self.mean) / self.stddev) ** 2)
        return t * t2
