#!/usr/bin/env python
import random as rnd
import rps
from collections import defaultdict

LOOKBACK = 4 #base move on last n moves
class MyClass:
    '''Uses a variety of predictor functions to predict each opponent's next move. 
    The most successful predictor is used each turn'''
    def __init__(self, name = 'duchowpt'):
        self.name = 'duchowpt'
        self.opponent_table = {}
        self.predictor_list = [Predictor('own moves markov', predict_based_on_own_markov), 
                                Predictor('their moves markov', predict_based_on_opp_markov), 
                                Predictor('random', predict_random_move),
                                Predictor('their frequency', predict_based_on_opp_frequency),
                                Predictor('both markov', predict_based_on_both_markov),
                                Predictor('rotate', predict_rotate)]
    def play(self, name):
        if name not in self.opponent_table:
            self.opponent_table[name] = Opponent(name)
        o = self.opponent_table[name]

        chosen_move = self.get_move(o)

        o.record_play(chosen_move)

        return chosen_move

    def get_move(self, opponent):
        ranked_predictors = sorted(self.predictor_list, key = lambda p: p.wins(opponent), reverse = True)
        for p in ranked_predictors:
            #print "{} ->\t{}".format(p.name, p.wins(opponent))
            p.last_prediction = p.predict(opponent)
        best_predictor = ranked_predictors[0]
        best_prediction = best_predictor.last_prediction
        counter_move = self.beat_move(best_prediction)
        return counter_move

    def learn(self, name, move):
        if name not in self.opponent_table:
            self.opponent_table[name] = Opponent(name)
        o = self.opponent_table[name]

        for p in self.predictor_list:
            prediction = p.last_prediction
            p_score, o_score, _ = rps.winner(self.beat_move(prediction), move)
            p.success_table[o] += (p_score-o_score)


        o.record_learn(move)
        
    def beat_move(self, move):
        return ((move + 1)%3)

    def print_prediction_results(self):
        for name, opponent in self.opponent_table.items():
            ranked_predictors = sorted(self.predictor_list, key = lambda p: p.wins(opponent), reverse = True)
            print "Predictors vs ", opponent.name
            for p in ranked_predictors:
                print "{:<20}{:>5}".format(p.name, p.wins(opponent))

class Opponent:
    '''Opponent is simply a record of everything we want to know about how
        we've reacted to this player'''
    def __init__(self, name):
        self.name = name
        self.moves = []
        self.move_frequency = {0:0, 1:0, 2:0}
        self.moves_table = {}
        self.ted_moves = [] # moves I've played against this opponent
        self.ted_table = {} #maps my moves to the reaction of this opponent
        self.clear_wins()

    def record_learn(self, move):
        
        #record this move based on the moves of this opponent
        if len(self.moves) > LOOKBACK:
            history = tuple(self.moves[-LOOKBACK:])
            if history in self.moves_table:
                self.moves_table[history].append(move)
            else:
                self.moves_table[history] = [move]

        self.moves.append(move) 

        #record this move based on the moves of duchowpt, 
        #note that this move matches with the most recent move in ted_moves, so we have to look slightly farther back 
        if len(self.ted_moves) > LOOKBACK:
            ted_history = tuple(self.ted_moves[-LOOKBACK-1:-1])#look slightly further back
            if ted_history in self.ted_table:
                self.ted_table[ted_history].append(move)
            else:
                self.ted_table[ted_history] = [move]

        #record this move in the frequency table
        #print "Move was actually ", move
        self.move_frequency[move] += 1
        #record the result
        ted_score, opp_score, _ = rps.winner(self.ted_moves[-1], move)
        self.ted_wins += ted_score
        self.ted_losses += opp_score
        self.games_played += 1

    def record_play(self, ted_move):
        self.ted_moves.append(ted_move)

    def clear_wins(self):
        self.ted_wins = 0
        self.ted_losses = 0
        self.draws = 0
        self.games_played = 0

class Predictor:
    '''Wrapper class for predictor function and success_table'''
    def __init__(self, name, predictor_func):
        self.name = name
        self.predict = predictor_func
        self.success_table = defaultdict(int)#map from opponent: score (wins-losses)
        self.last_prediction = 0

    def wins(self, opponent):
        return self.success_table[opponent]

def predict_based_on_own_markov(opponent):
    lookup = tuple(opponent.ted_moves[-LOOKBACK:])
    
    if lookup in opponent.ted_table:
        predicted_move = (rnd.choice(opponent.ted_table[lookup]))
    else:
        predicted_move = 0#always predict rock

    return predicted_move

def predict_random_move(opponent):
    return rnd.randint(0,2)

def predict_based_on_opp_markov(opponent):
    lookup = tuple(opponent.moves[-LOOKBACK:])
    
    if lookup in opponent.moves_table:
        predicted_move = rnd.choice(opponent.moves_table[lookup])
    else:
        predicted_move = 0#always predict rock

    return predicted_move

def predict_based_on_opp_frequency(opponent):
    freq_list = sorted(opponent.move_frequency.items(), key = lambda t: t[1], reverse = True)
    return freq_list[0][0]

def predict_based_on_both_markov(opponent):
    lookup = tuple(opponent.ted_moves[-LOOKBACK:])
    potential = []
    if lookup in opponent.ted_table:
        potential += opponent.ted_table[lookup]
    
    if lookup in opponent.moves_table:
   	    potential += opponent.moves_table[lookup]
    
    if potential:
        return rnd.choice(potential)
    else: return 0

def predict_rotate(opponent):
    try:
        return (opponent.ted_moves[-1]+1)%3
    except IndexError, e:
        return 0


if __name__ == '__main__':
    me = duchowpt()
    r = rps.Random()
    o = rps.Obsessive()
    t = rps.TitForTat()

    rps.play(me, r, 1000, True)

    # pl = [o, t, me, evan] 
    # rps.tournament(pl, 10000, True)