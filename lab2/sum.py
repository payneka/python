#!/usr/bin/env python

def sum_i(numbers):
    num_sum = 0
    for i in range(0,len(numbers)):
        num_sum = num_sum + numbers[i]

    return num_sum

def sum_r(num_sum):
    n = len(num_sum)
    if n == 1:
        return num_sum[0]
    else:
        return num_sum[0] + sum_r(num_sum[1:])
    

    

if sum_i([1,2,3]) != 6:
    print"Fix it"

if sum_i([.9,2.1,3]) != 6:
    print"Fix decimal"

if sum_i([1,2,3,-3]) !=3:
    print"Fix neg"

if sum_r([1,2,3]) != 6:
    print"Fix it R"

if sum_r([.9,2.1,3]) != 6:
    print"Fix decimal R"

if sum_r([1,2,3,-3]) !=3:
    print"Fix neg R"
    
print sum_i([1,2,3])
print sum_r([1,2,3])
