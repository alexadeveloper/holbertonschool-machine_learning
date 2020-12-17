#!/usr/bin/env python3
""" normal """


class Normal:
    """ class normal """

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
