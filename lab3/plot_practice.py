#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

def sinf(nrange):
    return np.sin(nrange)

nrange = np.arange(0.0, 4.0*np.pi, 0.1)
plt.plot(nrange, sinf(nrange), 'b')
plt.axis([0,12,-1,1])
plt.show()
