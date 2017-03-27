#!/usr/bin/env python


from random import randint
import collections

class payneka:
    def __init__(self, name='payneka'):
        self.name = name
        self.move = randint(0,2)
        #self.prev_oppmoves = []
        #self.prev_moves = []
        r,p,s = 0,1,2
        self.n = 50 #length of movelist to check
        self.patlen = 1 #length of pattern to check
        self.movelist = []
        self.prevmove = self.move
        
    def play(self,name):
        return self.move
        
        
    def learn(self,opp_name,opp_move):
        self.movelist.append([self.prevmove, opp_move])
        opp_likely_mv = [0,0,0]
        #if # of entries in movelist is greater than the desired patern length +1
        if len(self.movelist) > self.patlen+1:
            #for loop repeat along each element in move list starting at 0, ending at len(movelist) minus the patern length
            for i in range(0,len(self.movelist)-self.patlen):
                #if the last patlen elements in movelist match the current movelist element
                if self.movelist[len(self.movelist)-self.patlen:len(self.movelist)] == self.movelist[i:i+self.patlen]:
                    opp_likely_mv[self.movelist[i+self.patlen][1]] += 1
                    #print opp_likely_mv
    
        
        self.move = opp_likely_mv.index(max(opp_likely_mv)) +1
        #print self.move
        if self.move == 3:
            self.move = 0
        return self.move
        
        #self.move = randint(0,2)     
            
        #Counters based on known opponent names / types:
##        if opp_name == 'Obsessive': 
##            if opp_move == 0:
##                self.move = 1                
##            elif opp_move == 1:
##                self.move = 2                
##            else:
##                self.move = 0   
##
##
##        elif opp_name == 'TitForTat':
##            if self.move == 0 :
##                self.move = 1                
##            elif self.move ==1:
##                self.move = 2                
##            else:
##                self.move = 0
##
##        else:
##            for element in 

    
