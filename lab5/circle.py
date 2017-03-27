#!/usr/bin/env python

import numpy as np

class circle(object):
    def __init__(self, r):
        self.r = r

    def area(self):
        return(np.pi*self.r**2)

    def diameter(self):
        return(self.r*2)

    def circumference(self):
        return(2*self.r*np.pi)

c = circle(3.0)

