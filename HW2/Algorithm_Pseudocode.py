#RPS Algorithm:
#depending on success, may want to add in randomness (either winning move or tying move)
#Setup code:
#n = length of list to check
#patlen = length of pattern to check (last pat elements determine move)
#patterns = {list of all possible patterns to look for, based on patlen}

#Learn Code
#Opponent move preditiction: 
#add [mymove, oppmove] to movelist
#opponent_likely_move = [0,0,0]
#if len(list) > n elements:
        #for last n elements in movelist - patlen:
            #if (last patlen elements) == movelist[i:i+patlen]:
                #check opponent move of next element in movelist (returns 0,1,2)
                #opponent_likely_move{previousline) =+1 #adds 1 to score of corrisponding move, keeps track of most likely next move 

#else:
    #for every element in list:
        #copy of above code
        

#mymove modification
#mymove = move to beat oponent, based on opponent_likely_move
#If losing:
    #mymove = mymove+2 #choose opposite of normal

#Fix addition stuff
#If mymove == 4:
        #mymove = 1
#elif mymove == 3:
        #mymove = 0
