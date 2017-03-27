#!/usr/bin/env python

from complex import *
import numpy as np

def roots(a=0, b=0, c=0):
    square = b**2-4*a*c
    if square < 0:
        real = -b/(2*a)
        imag = abs(square)**(1.0/2.0)/(2*a)
        return (Complex(real, imag),Complex(real,-imag))
        
    else:
        return ((-b+(square)**(1.0/2.0))/(2*a), (-b-(square)**(1.0/2.0))/(2*a))

print roots(1,2,3)
print roots(1,4,1)
