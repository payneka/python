#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import timeit


list1 = np.random.random_sample(10)


def bubblesort(list1):
    for n in range(len(list1)):
        for i in range(len(list1)-n):
            if i == len(list1)-1:
                None
            elif list1[i] > list1[i+1]:
                list1[i],list1[i+1] = list1[i+1],list1[i]
            else:
                None

    return list1



def sorttime():
    sorttime = np.arange(0,10)
    for i in range(10):
        sorttime
        sortstart = timeit.time.time()
        bubblesort(list1)
        sortend = timeit.time.time()
        sorttime[i] = sortend-sortstart
        
    sortavg = np.average(sorttime)
    return(sortavg)

def is_sorted(sort_list):
    count = 0
    for i in range(len(sort_list)-1):
        if sort_list[i] <= sort_list[i+1]:
            count = count+1
        else:
            None
    if count == len(sort_list)-1:
        return True
    else:
        return False

#print is_sorted(bubblesort(list1))


    
    

                   
