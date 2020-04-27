# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:29:14 2020

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt


axis1 = plt.subplot(3,1,1)
axis1.plot([10, 20, 23, 40,50,66])
#axis1.ylabel('some numbers')
axis1.grid()
plt.show()


mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

axis2 = plt.subplot(3,1,2)
# the histogram of the data
[n, bins, patches] = axis2.hist(x, 50, density=1, facecolor='g', alpha=0.75)


#axis2.xlabel('Smarts')
#axis2.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#axis2.axis([40, 160, 0, 0.03])
axis2.grid(True)
plt.show()


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)


axis3 = plt.subplot(312)
axis3.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

axis4 = plt.subplot(313)
axis4.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
