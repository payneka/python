#!/usr/bin/env python
import math

def estimate_pi():
    k=0
    sum_term = 1
    last_term = 1
    while last_term >= 1e-15:
        last_term = (math.factorial(4*k)*(1103+26390*k))/(math.factorial(k)**4*396**(4*k))
        #print last_term
        sum_term = sum_term + last_term
        #print sum_term
        k = k+1

    return 1/((2*math.sqrt(2))/9801*sum_term)

if math.fabs(estimate_pi() - math.pi) <= .1:
    print estimate_pi()
    print math.pi
    print("It's all good")
else:
    print estimate_pi()
    print math.pi
    print("It's all bad!")
        
