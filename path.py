'''
@author:Chaoxiang  Ye 
    11.03.2021

'''
from cliff import x_range, y_range, actions
from table import q_table
import numpy as np

def observe(x,y,a):
    goal=0
    if x==x_range-1 and y==0:
        goal=1
    if a==0:
        y+=1
    if a==1:
        y-=1
    if a==2:
        x-=1
    if a==3:
        x+=1
    x=max(0,x)
    x=min(x_range-1,x)
    y=max(0,y)
    y=min(y_range-1,y)
    if goal==1:
        return x,y,-1
    if x>0 and x<x_range-1 and y==0:
        return 0,0,-100
    return x,y,-1

def OptimalPath(q_table):
    V=[]
    for k,v in q_table.items():
        V.append(v)

    v_table=np.zeros([12,4,4])
    for i in range(12):
        for j in range(4):
            for z in range(4):
                v_table[i][j][z]=V[z+(4*j)+(16*i)]

    x=0
    y=0
    path=np.zeros([12,4])-1
    end=0
    exist=np.zeros([12,4])
    while(x!=x_range-1 or y!=0) and end==0:
        a=np.argmax(v_table[x][y])
        path[x][y]=a
        if exist[x][y]==1:
            end=1
        exist[x][y]=1
        x,y,r=observe(x,y,a)
    for j in range(y_range-1,-1,-1):
        for i in range(x_range):
            if i==x_range-1 and j==0:
                print('G',end='')
                continue
            a=path[i][j]
            if a==-1:
                print(" 0 ",end="")
            elif a==0:
                print("↑",end="")
            elif a==1:
                print("↓",end="")
            elif a==2:
                print("←",end="")
            elif a==3:
                print("→",end="")
        print(' ')