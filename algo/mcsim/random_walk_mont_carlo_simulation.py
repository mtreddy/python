#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
def random_walk(n):
    """Random walk co-ordinates after n walks"""
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N','S','E','W'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        else:
            x = x -1
    return (x, y)

for i in range(25):
    walk = random_walk(10)
    print(walk, "Distance from home=", abs(walk[0]) + abs(walk[1]))


# In[2]:


def random_walk1(n):
    """Return cooardinates after 'n' block random walk."""
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy
    return (x,y)
for i in range(25):
    walk = random_walk(10)
    print(walk, "Distance from home=", abs(walk[0]) + abs(walk[1]))


# In[5]:


no_of_walks = 20000
for walk_len in range(1, 31):
    no_tr = 0
    for i in range(no_of_walks):
        (x, y) = random_walk1(walk_len)
        dist = abs(x) + abs(y)
        if dist <= 4:
            no_tr += 1
    no_tr_percentage = float(no_tr)/no_of_walks
    print("walk sze =", walk_len, "/% of no tr =", 100*no_tr_percentage)
    


# In[ ]:




