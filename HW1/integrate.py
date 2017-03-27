#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def integrate(y,a,b,n=.001):

    #swap a, b if a>b:
    if a > b:
        a,b = b,a

    areas = []
    x = a+n/2
    while x <= b:
        x += n
        areas.append(y(x)*n) #creates list of rieman areas

    return sum(areas)#returns reiman sum


f = lambda x: 3*x**2+2*x+1
a = 2.0
b = 4.0
n = .0001
#print integrate(f,a,b,n)
    
actual_int = 70
dif = []
n_val =  np.arange(.0001,1,.001)
#print n_val
for element in n_val:
    dif.append(np.abs(actual_int-integrate(f,a,b,element)))
    #integration is correct, graph behaving strangly, no idea why

#print dif
plt.plot(n_val,dif,'b')
plt.show()
