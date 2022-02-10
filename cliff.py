'''
@author:Chaoxiang  Ye 
    11.03.2021

'''
#cliff range:x=12;y=4
x_range=12
y_range=4


#action option:up,down,left,right
actions=["up", "down", "left", "right"]


# state:(x,y)
# action: up、down、left、right
# return ((x,y),rewards,end_flag)
def next_state_reward_end(state, action):
    """  initial state coordinates:（0,0），absorption state coordinates:（x_range-1, 0）"""
    # current state coordinates: ( x, y)  next state coordinates:( next_x, next_y)
    x, y=state
    
    end_flag=False
    
    if action=="up":
        next_x=x
        next_y=y+1
    elif action=="down":
        next_x=x
        next_y=y-1
    elif action=="left":
        next_x=x-1
        next_y=y
    elif action=="right":
        next_x=x+1
        next_y=y


    # Abosorption state judgment
    if next_x==x_range-1 and next_y==0:
        reward=-1
        end_flag=True
        return (next_x, next_y), reward, end_flag


    # Wall judgment
    if next_x<0 or next_x>(x_range-1) or next_y<0 or next_y>(y_range-1):
        next_x, next_y=x, y    
        reward=-1 
        end_flag=False
        return (next_x, next_y), reward, end_flag


    # cliff judgment
    if 0<next_x<(x_range-1) and next_y==0:
        next_x, next_y=0, 0 
        reward=-100
        end_flag=False
        return (next_x, next_y), reward, end_flag


    # normal state judgment
    reward=-1
    end_flag=False
    return (next_x, next_y), reward, end_flag
