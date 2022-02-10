'''
@author:Chaoxiang  Ye 
    11.03.2021

'''

from cliff import x_range, y_range, actions

q_table=dict()

#  initialize Q_table
def q_table_init():
    q_table.clear()
    for i in range(x_range):
        for j in range(y_range):
            for action in actions:
                q_table[((i, j), action)]=0 