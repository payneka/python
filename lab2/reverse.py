#!/usr/bin/env python

def reverse_r(list_input):
    return None

def reverse_i(list_input):
    list_reverse = list_input[:]
    for n in range(0,len(list_input)):
        list_reverse[n] = list_input[(len(list_input)-1-(n))]
        
    return list_reverse

def reverse_r(list_input):
    if len(list_input) == 0:
        return rev_list
    else:
        print rev_list
        rev_list = [(reverse_r(list_input[len(rev_list)+1:]))] + [rev_list[0]]
         
if reverse_r([1,2,3]) != [3,2,1]:
    print("Fix #s R")
if reverse_r(["a","b","c"]) != ["c","b","a"]:
    print("Fix letters R")
if reverse_r(["a",2,"b"]) != ["b",2,"a"]:
    print("Fix mix R")
if reverse_i([1,2,3]) != [3,2,1]:
    print("Fix #s I")
if reverse_i(["a","b","c"]) != ["c","b","a"]:
    print("Fix letters I")
if reverse_i(["a",2,"b"]) != ["b",2,"a"]:
    print("Fix mix I")
