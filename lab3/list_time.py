#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import timeit

list1 = np.random.random_sample(1)
list2 = np.random.random_sample(10)
list3 = np.random.random_sample(100)
list4 = np.random.random_sample(1000)
list5 = np.random.random_sample(10000)
list6 = np.random.random_sample(100000)
list7 = np.random.random_sample(1000000)

listset = [list1,list2,list3,list4,list5,list6,list7]
listnum = np.arange(0,7,1)

def sorttime(listset):
    
    for  i in range(len(listset)):
        listset[i] = sorted(listset[i])
        

    return sorttime

def sumtime(listset):
    for i in range(len(listset)):
        listset[i] = sum(listset[i])
        #timing function goes here

    return sumtime

sortt = sorttime(listset)
sumt = sumtime(listset)

plt.plot(sortt,listnum)
plt.axis([0,7, 0, #max sort time)
plt.show()

plt.plot(sumt,listnum)
plt.axis([0,7,0,#max sum time)
plt.show()


