#!/usr/bin/env python

def letter_count (string,letter):
    lettercount = 0
    string = str.lower(string) #str.lower converts all to lowercase
    letter = str.lower(letter)
    
    for i in range(0,len(string)): #for every element in string 
        if string[i] == letter:
            lettercount = lettercount+1 #counts number of matching letters
    return lettercount

string = "halLway"
letter = "l"

print letter_count(string, letter)
