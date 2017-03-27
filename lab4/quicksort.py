#!/usr/bin/env python

import numpy as np
#implemented from hetland.org/coding/python/quicksort.html
#Source also includes interactivepython.org/runestone/static/pythonds/sortsearch/thequicksort.html

def split(list1, begin, end):
    split_pt = list1[end] 
    left_index = begin-1
    right_index = end
    is_split = 0
    while is_split == 0:
        while is_split ==0:
            left_index = left_index+1

            if left_index == right_index:
                is_split = 1
                break

            if list1[left_index] > split_pt:
                list1[right_index] = list1[left_index]
                break

        while is_split ==0:
            right_index = right_index-1

            if right_index == left_index:
                is_split = 1
                break

            if list1[right_index] < split_pt:
                list1[left_index] = list1[right_index]
                break

    list1[right_index] = split_pt
    #print(list1)
    return right_index

def sorting(list1, begin, end):

    if begin < end: 
        halfway_pt = split(list1,begin, end)
        sorting(list1, begin, halfway_pt-1)
        sorting(list1, halfway_pt+1, end)
    else:
        return (list1)


list1 = np.random.random_sample(10)
sort = sorting(list1, 0, len(list1)-1)



    
        
    
    
