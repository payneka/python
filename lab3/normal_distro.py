#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

def samplesum():
    randnum = np.arange(0.0,10.0,1)
    randsum = np.arange(0.0,100000.0,1)
    for n in range(len(randsum)): #sums each list of samples, adds to a list
        for i in range(len(randnum)): #creates sample list of 10 random values
            randnum[i] = np.random.random_sample(1.0)
        
        randsum[n] = sum(randnum)
    return randsum


randsum = np.sort(samplesum())
plt.hist(randsum, bins=1000)
plt.axis([2,8,0,500])
plt.xlabel('Bins')
plt.ylabel('Number of occurances')
plt.show()

    
