#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import timeit
from sort import bubblesort
from quicksort import sorting


#Random list generator
length_list = np.arange(100,2100,100)
sample_list = []

for i in range(len(length_list)):
    sample_list.append(np.random.random_sample(length_list[i]))


#tests bubblesort for each list
time_list_bubble = []
time_list_sorted = []
time_list_quick = []
for n in range (len(length_list)):
    #bubblesort time
    sortstart = timeit.time.time()
    bubblesort(sample_list[n])
    sortend = timeit.time.time()
    time_list_bubble.append(sortend-sortstart)
    #sorted time
    sortstart1 = timeit.time.time()
    sorted(sample_list[n])
    sortend1 = timeit.time.time()
    time_list_sorted.append(sortend1-sortstart1)
    #quicksort time
    sortstart2 = timeit.time.time()
    sorting(sample_list[n], 0, len(sample_list[n])-1)
    sortend2 = timeit.time.time()
    time_list_quick.append(sortend2-sortstart2)
    


plt.plot(length_list, time_list_bubble, 'r', length_list, time_list_sorted, 'b', length_list, time_list_quick, 'g' )
plt.show()

