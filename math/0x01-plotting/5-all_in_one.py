#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

plt.title("All in One")
plt.subplots_adjust(wspace=0.5, hspace=1)

g1 = plt.subplot(321)
g1 = plt.autoscale(axis='x', tight=True)
g1 = plt.plot(y0, 'r')

g2 = plt.subplot(322)
g2.set_title("Men's Height vs Weight", fontsize='x-small')
g2.set_xlabel('Height (in)', fontsize='x-small')
g2.set_ylabel('Weight (lbs)', fontsize='x-small')
g2 = plt.scatter(x1, y1, s=5, c='m')

g3 = plt.subplot(323)
g3.set_title("Exponential Decay of C-14", fontsize='x-small')
g3.set_xlabel('Time (years)', fontsize='x-small')
g3.set_ylabel('Fraction Remaining', fontsize='x-small')
g3 = plt.xlim(0, 28650)
g3 = plt.yscale('log')
g3 = plt.plot(x2, y2)

g4 = plt.subplot(324)
g4.set_title("Exponential Decay of Radioactive Elements", fontsize='x-small')
g4.set_xlabel('Time (years)', fontsize='x-small')
g4.set_xlim(0, 20000)
g4.set_ylabel('Fraction Remaining', fontsize='x-small')
g4.set_ylim(0, 1)
g4.plot(x3, y31, 'r--', label='C-14', fontsize='x-small')
g4.plot(x3, y32, 'g', label='Ra-226', fontsize='x-small')
g4.legend()

plt.show()
