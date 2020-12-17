#!/usr/bin/env python3
""" bynomial """


class Binomial:
    """ class bynomial """

    def __init__(self, data=None, n=1, p=0.5):
        """ constructor """
        if data is None:
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            if n <= 0:
                raise ValueError("n must be a positive value")
            self.n = int(n)
            self.p = float(p)
        else:
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            if type(data) != list:
                raise TypeError("data must be a list")
            m = float(sum(data) / len(data))
            st = sum([(data[j] - m) ** 2 for j in range(len(data))])
            std = st / len(data)
            self.p = 1 - (std / m)
            self.n = int(round(m / self.p))
            self.p = m / self.n

    def pmf(self, k):
        """ pmf """
        if type(k) != int:
            k = int(k)
        if k > self.n or k < 0:
            return 0
        nf = 1
        for j in range(1, self.n + 1):
            nf *= j
        kf = 1
        for l in range(1, k + 1):
            kf *= l
        tf = 1
        for m in range(1, (self.n - k) + 1):
            tf *= m
        t2 = nf / (kf * tf)
        return t2 * ((self.p ** k) * ((1 - self.p) ** (self.n - k)))
