#!/usr/bin/env python


from random import randint
import collections

class payneka:
    def __init__(self, name='payneka'):
        self.name = name
        self.move = randint(0,2)
        self.prev_oppmoves = []
        self.prev_moves = []

    def play(self,name):
        return self.move
        
        
    def learn(self,opp_name,opp_move):
        self.prev_oppmoves.append(opp_move)
        occurance = {}
        for element in self.prev_oppmoves:
            if element in occurance:
                occurance[element] +=1
            else:
                occurance[element] = 1
        occurance = sorted(occurance, key = occurance.get, reverse = True)
        print occurance
        #Counters based on known opponent names:
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
                
##        if:
            #Plays based on freqency of opponent's previous moves
        
        elif occurance[0] == 0:
            self.move = 1
        elif occurance[0] == 1:
            self.move = 2
        elif occurance[0] == 2:
            self.move = 0
            

            
        
        self.prev_moves.append(self.move)
        
                    
        #print self.prev_moves
        #Counters based on unknown opponent names, but known opponent types:
        
        
