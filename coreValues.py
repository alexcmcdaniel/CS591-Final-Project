# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 14:08:03 2018

@author: Owner
"""

import itertools
import numpy as np


def value(subset):
    """
    GAME WHERE $100 IS SPLIT BETWEEN
    A JOB WHERE AT LEAST 3 WORKERS ARE NEEDED
    AND ALL ARE PAID EQUALLY. VALUE RETURNS
    THE PAY OFF TO EACH MEMBER OF THE COALITION
    """
    if len(subset) >= 3:
        return 100/len(subset)
    else:
        return 0
        


def coreValues(n_players):

    combs = []
    for x in range(1, len(n_players)):
        combs += list(itertools.combinations(n_players, x))

    combs = combs[1:]
    #combs = list(itertools.chain(*combs))

    combs = combs[:-1]
    grand_coalition = [n_players, value(n_players)]
    
    payoffs = []
    for x in combs:
        payoffs.append([x, value(x)])
    
    core = []
    for payoff in payoffs:
        if payoff[1] >= grand_coalition[1]:
            core.append(payoff)
            
    return core
            
        
        
    
    
    
if __name__ == '__main__':
    n_players = ('A', 'B', 'C', 'D')
    print("INPUTTING COALITION: ", n_players)
    print(coreValues(n_players))
    
    
"""
FOR THIS PROBLEM, THE COALITION
OF UN COUNCIL WILL ONLY PASS THE BILL
AT LEAST 3 OF 5 AGREE, LEAVING
A VALUE OF 1, OTHERWISE 0 IF NOT PASSED
"""