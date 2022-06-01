#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Imports 

import random
import matplotlib.pyplot as plt
from math import e


# In[12]:


# Create Initial State

N = 10000 #number of spins

initial_state = []

for i in range(N):
    a = random.randint(0,1)
    if(a ==0):
        initial_state.append(-1)
    else:
        initial_state.append(1)


# In[13]:


#Energy calculation function

def calculate_energy(state):
    energy = 0
    J = 1
    
    for i in range(N):
        energy += J * state[i-1] * state[i]
    
    return(energy)


# In[14]:


def change_in_energy(prev_state, state):
    diff = calculate_energy(state) - calculate_energy(prev_state)
    return(diff)


# In[15]:


M = 1000000 #number of times we select a candidate
ticks = [] #to keep track of time

energy_values = [] #energy of the system at each tick

T = 2.15 #temperature


for i in range(M):
    candidate = random.randint(0, N-1)

    new_state = initial_state
    new_state[candidate] = new_state[candidate]*(-1)
    change = change_in_energy(initial_state, new_state)
    if(change <= 0):
        initial_state = new_state

    else:
        b = random.random()
        if(b <= e**(change/(1.38*(10**-23))/T)):
            initial_state = new_state
    energy_values.append(calculate_energy(initial_state))
    ticks.append(i)


# In[10]:


plt.plot(ticks, energy_values)


# In[ ]:




