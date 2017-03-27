#!/usr/bin/env python


from random import randint
import collections

class MyPlayer:
    def __init__(self, name='payneka'):
        self.name = name
        self.move = randint(0,2)
        self.n = 20#length of movelist to check. If running slow, feel free to adjust this to 10 (doesn't work as well)
        patternlength = 10 #Max length of pattern to check
        self.patlen = range(1,patternlength+1) 
        self.movelist = []
        self.score = 0
        
    def play(self,name):
        return self.move
        
        
    def learn(self,opp_name,opp_move):
        self.movelist.append([self.move, opp_move])
        #scorekeeper
        if (self.move == opp_move+1 or self.move+2 == opp_move):
            self.score = self.score+1
        elif self.move == opp_move:
            None
        else:
            self.score = self.score-1

        #Main pattern recognition algorithm. Predicts next play based on previous patterns, from previous up to patternlength sets     
        opp_likely_mv = [0,0,0]
        for p in range(len(self.patlen)):
            if len(self.movelist) > self.patlen[p]+1: #if num of entries in movelist is greater than the desired patern length +1
                rangebot = max(0,len(self.movelist)-self.n) #sets minimum of scan range 
                for i in range(rangebot,len(self.movelist)-self.patlen[p]): #along each element in move list starting at 0, ending at len(movelist) minus the patern length
                    if self.movelist[len(self.movelist)-self.patlen[p]:len(self.movelist)] == self.movelist[i:i+self.patlen[p]]: #if the last patlen elements in movelist match the current movelist element
                        opp_likely_mv[self.movelist[i+self.patlen[p]][1]] += 1        
        
        self.move = opp_likely_mv.index(max(opp_likely_mv)) + 1  

        #alternative strategies:
        if self.score < -1:
            self.move = self.move + randint(0,1) #attempts to tie or win, should throw off prediction algorithms a bit. 
            if self.score < -2:
                self.move = self.move + randint(0,1)

        #move fixing for addition simplification
        if self.move == 3:
            self.move = 0
        elif self.move == 4:
            self.move =1
        elif self.move == 5:
            self.move =2
            
        return self.move
          

    
