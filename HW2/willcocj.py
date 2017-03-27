#!/usr/bin/env python

from rps import *
from game import *
from random import randint
import string


class MyPlayer:
	def __init__(self, name='willcocj'):
		self.name = name
		self.my_move = 0
		self.move_history = []
		self.op_hist = []
		self.op_type = []
		self.counter = 0
		self.opponent = 3
		self.p0_finish = [0, 2, 1] # Will iterate through backwards
		self.p1_finish = [2]
		self.p2_finish = [0]
		self.p4_finish = [1]
		self.p5_finish = [2, 1, 0] # Will iterate through backwards
		self.p6_finish = [0, 2, 1] # Will iterate through backwards



	def play(self, name):
		# My play code is in here
		#print name
		self.move_history.append(self.my_move)

		#print 'my moves:', self.move_history
		return self.my_move
		
		

	def learn(self, name, move):
		self.op_hist.append(move)
		#if self.op_hist(0)
		rnd = len(self.op_hist)		
		#print self.op_hist, 'round:', rnd, self.op_hist[0]

		if rnd == 1: # Round 2 decision making
			#print 'Making decision for round 2'

			if self.op_hist[0] == 0:
				self.my_move = 1
				return self.my_move

			elif self.op_hist[0] == 1:
				self.my_move = 1
				return self.my_move

			elif self.op_hist[0] == 2:
				self.my_move = 0
				return self.my_move


		elif rnd == 2: # Round 3 decision making
			#print 'Making decision for round 3'

			if self.op_hist[0] == 0 and self.op_hist[1] == 0:
				# opponent is unknown
				self.my_move = 1
				return self.my_move

			elif self.op_hist[0] == 1 and self.op_hist[1] == 0:
				# opponent is probably playing TitForTat 
				self.opponent = 0
				self.op_type.append(0)
				self.my_move = 2 # Play(0,1,2) repeating after this
				#print 'player:', self.opponent
				return self.my_move

			elif self.op_hist[0] == 1 and self.op_hist[1] == 1:
				# opponent is probably playing Obsessive
				self.opponent = 1
				#print 'player is obsessed with paper'
				self.op_type.append(1)
				self.my_move = 2 # Play(2)->
				#print 'player:', self.opponent
				return self.my_move

			elif self.op_hist[0] == 2 and self.op_hist[1] == 0:
				# opponent is unknown
				self.my_move = 1
				return self.my_move

			elif self.op_hist[0] == 2 and self.op_hist[1] == 2:
				# opponent is probably playing Obsessive
				self.opponent = 2
				#print 'player is obsexxed with scissors'
				self.op_type.append(2) 
				self.my_move = 0 # Play(0)->
				#print 'player:', self.opponent
				return self.my_move

			else:
				# opponent is random or some other pattern
				self.opponent = 3
				self.op_type.append(3)
				self.my_move = randint(0,2) # Play radomly for a while
				#print 'player:', self.opponent
				return self.my_move


		elif rnd == 3 and self.opponent >= 3: # Round 4 desicion making
			#print 'Making decision for round 4'

			if self.op_hist[0] == 0 and self.op_hist[1] == 0 and self.op_hist[2] == 0:
				# opponent is probably playing Obsessive
				self.opponent = 4
				#print 'player is obsessed with rock'
				self.op_type.append(4)
				self.my_move = 1 # Play(1)->
				#print 'player:', self.opponent
				return self.my_move

			elif self.op_hist[0] == 0 and self.op_hist[1] == 0 and self.op_hist[2] == 1:
				# opponent is probably playing TitForTat 
				self.opponent = 5
				self.op_type.append(5)
				self.my_move = 1 # Play(2,0,1) repeating after this
				#print 'player:', self.opponent
				return self.my_move

			elif self.op_hist[0] == 2 and self.op_hist[1] == 0 and self.op_hist[2] == 0:
				# opponent is probably playing TitForTat, 
				self.opponent = 6
				self.op_type.append(6)
				self.my_move = 2 # Play (0,1,2) repeating after this
				#print 'player:', self.opponent
				return self.my_move

			else:
				# opp is random or some other pattern
				self.opponent = 7
				self.op_type.append(7)
				self.my_move = randint(0,2) # Play radomly for a while
				#print 'player:', self.opponent
				return self.my_move

		else:
			if self.opponent == 0:
				#print 'in player 0 finale'
				self.my_move = self.p0_finish[0]
				self.counter -= 1
				return self.my_move

			elif self.opponent == 1:
				#print 'in player 01 finale'
				self.my_move = self.p1_finish[0]
				return self.my_move

			elif self.opponent == 2:
				#print 'in player 2 finale'
				self.my_move = self.p2_finish[0]
				return self.my_move

			elif self.opponent == 3:
				#print 'in player 3 finale'
				self.my_move = randint(0,2) # Play randomly against random and unknown types
				return self.my_move

			elif self.opponent == 4:
				#print 'in player 4 finale'
				self.my_move = self.p4_finish[0]
				return self.my_move

			elif self.opponent == 5:
				#print 'in player 5 finale'
				self.my_move = self.p5_finish[0]
				self.counter -= 1
				return self.my_move

			elif self.opponent == 6:
				#print 'in player 6 finale'
				self.my_move = self.p6_finish[0]
				self.counter -= 1
				return self.my_move

			elif self.opponent == 7:
				#print 'in player 7 finale'
				self.my_move = randint(0,2) # Play randomly against random and unknown types
				return self.my_move







		







