#!/usr/bin/env python


from rps import *
import payneka
import willcocj
import duchowpt

if __name__ == '__main__':
    players = [Obsessive(), TitForTat(), payneka.MyPlayer()]
    
    tournament(players, 10000, False)
    tournament(players, 10000, True)
    
