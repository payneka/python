#!/usr/bin/env python

import numpy as np
import string, re

#sources:
#http://stackoverflow.com/questions/18135967/creating-a-list-of-every-word-from-a-text-file-without-spaces-punctuation
#http://stackoverflow.com/questions/13707457/python-value-that-occurs-the-most-in-a-list

class Book:
    def __init__(self, filename):
        self.file = open(filename, 'r') #reads in txt file
        text = self.file.read().lower()
        self.file.close()

        self.wc = list(text.split()) #List for word count funciton     
        text = re.sub('[^a-z\ \']+', " ", text)
        self.words = list(text.split()) #List for comparison (no punctiuation)
        self.words = sorted(self.words) #creates sorted list of words
        #print self.words[1:1000]
        self.unique = set(self.words) #This was speed improvement (removes duplicates)

        print 'Text Imported'
        #print self.unique
        
                    
    def number_of_words(self):
        return len(self.wc)

    def common_words(self,n):
        occurance = {}
        for element in self.words:
            if element in occurance:
                occurance[element] +=1
            else:
                occurance[element] = 1
                
        occurance = sorted(occurance, key = occurance.get, reverse = True)
        return occurance[0:n]
    
    def __sub__(self,other):
        print 'There are %g words in first text not in second text'% len(list(self.unique-other.unique))
        #print list(self.unique-other.unique)
if __name__ == "__main__":
    
    book = Book('war_and_peace.txt')
    dic = Book('american-english.txt')
    print 'Linux WC = 566308 \nCustom word count'
    print book.number_of_words()
    book - dic
    print 'End of Code'
    print book.common_words(6)
    
    
