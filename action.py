'''
@author:Chaoxiang  Ye 
    11.03.2021

'''

import random
from cliff import actions   
from table import q_table  



def _action(state, act_str):
    q_value_list=[]
    for action in actions:
        q_value_list.append( (action, q_table[(state, action)]) ) 
    
    if act_str=="greedy":
        random.shuffle(q_value_list)
        q_value_list.sort(key=lambda x:x[1])
        return q_value_list[-1] 
    elif act_str=="random":
        return random.choice(q_value_list)
    
    
# greedy
def greedy_action(state):
    return _action(state, "greedy")


# epsilon-greedy
def epsilon_action(state,epsilon):
    if random.random()>epsilon:
        return _action(state, "greedy")
    else:
        return _action(state, "random")