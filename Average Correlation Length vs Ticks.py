#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Imports 

import random
import matplotlib.pyplot as plt
from math import e


# In[6]:


N = 10000 #number of spins

initial_state = []

for i in range(N):
    a = random.randint(0,1)
    if(a ==0):
        initial_state.append(-1)
    else:
        initial_state.append(1)


# In[7]:


#Energy calculation function

def calculate_energy(state):
    energy = 0
    J = 1
    
    for i in range(N):
        energy += J * state[i-1] * state[i]
    
    return(energy)


# In[8]:


def change_in_energy(prev_state, state):
    diff = calculate_energy(state) - calculate_energy(prev_state)
    return(diff)


# In[9]:


def avg_correlation_length(state):
    lengths = []
    k = 0
    a = 0
    for i in range(N-1):
        if(state[i] == state[i+1]):
            k = k+1
        else:
            lengths.append(k)
            k = 0
            a = a+1
    avg = sum(lengths) / a
    
    return(avg)


# In[10]:


M = 100000 #number of times we select a candidate
ticks = [] #to keep track of time

avg_corr_lengths = [] #average correlation lengths at each tick

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
    avg_corr_lengths.append(avg_correlation_length(initial_state))

    ticks.append(i)


# In[ ]:




