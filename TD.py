'''
@author:Chaoxiang  Ye 
    11.03.2021

'''

from cliff import next_state_reward_end
from table import q_table
from action import epsilon_action, greedy_action


# Discount parameter
lam=1

# learning rate
lr=0.1


def q_learning(state,epsilon):
    # epsilon-greedy choose the action of the current state
    action, q = epsilon_action(state,epsilon)
    
    # next state. reward, and end flag
    next_state, reward, end_flag=next_state_reward_end(state, action)   

    # evaluation next action of next state
    next_action, next_q=greedy_action(next_state)
 
    #estimate the current action value 
    estimate=reward+lam*next_q
    
    #TD error
    td_error = estimate - q
    
    #update the current action value
    q_table[(state, action)]+=lr*td_error
    
    return next_state, reward, end_flag 


def sarsa_learning(state,epsilon):
    # epsilon-greedy choose the action of the current state(same as q_learning)
    action, q = epsilon_action(state,epsilon)
    
    #  next state. reward, and end flag
    next_state, reward, end_flag=next_state_reward_end(state, action)   

    #  evaluation next action of next state(different from q_learning)
    next_action, next_q=epsilon_action(next_state,epsilon)
 
    #estimate the current action value 
    estimate=reward+lam*next_q
    
    #TD error
    td_error = estimate - q
    
    #update the current action value
    q_table[(state, action)]+=lr*td_error
    
    return next_state, reward, end_flag 

