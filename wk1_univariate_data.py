# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:15:16 2020
@author: chris.cirelli
"""

# Import Python Libraries -----------------------------------
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import pylab

# Create a Vector of Random Variables from Normal Dist
def gen_ran_norm_vals(num):
    ran_norm = stats.norm.rvs(size=num)
    plt.hist(ran_norm)
    plt.show()
    
    
def gen_cdf_ran_data():
    dx = 0.01
    X = np.arange(-2, 2, dx)
    Y = pylab.exp(-X**2)  # creates bell shape curve. 
    cy = np.cumsum(Y*dx)
    pylab.plot(X, Y)
    pylab.plot(X, cy, 'r--')
    pylab.show()


x = np.arange(0, 10, 0.1)

plt.plot(x, np.sin(x))



