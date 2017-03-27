#!/usr/bin/env python

import numpy as np
from random import uniform

#sources:
#http://stackoverflow.com/questions/8287167/python-generate-random-number-between-x-and-y-which-is-a-multiple-of-5
#http://codereview.stackexchange.com/questions/69370/monte-carlo-pi-calculation

def area(f, pt1, pt2, q=1e6):

    corners = [0,0] #not really corners, just keeps track of the points
    for y in range(int(np.sqrt(q))):
        for x in range(int(np.sqrt(q))):
            p0s = uniform(pt1[0],pt2[0])#uniform distro between 2 points
            p1s = uniform(pt1[1],pt2[1])
            xy = (p0s,p1s) #combines points to 1 variable
            if f(xy[0],xy[1]) > 0:
                corners[1] +=1

            else:
                corners[0] +=1

    Area = (pt2[1] - pt1[1])*(pt2[0]  - pt1[0])
    est_area = corners[0]/q*Area

    return est_area

#used similar values to classmates to comapre answers
f = lambda x,y: x*x + y*y -1
pt1 = (-1,-1)
pt2 = (1,1)
print area(f, pt1, pt2)                          

        
