#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Imports 

import random
import matplotlib.pyplot as plt
from math import e



# In[9]:


N = 10000 #number of spins

initial_state = []

for i in range(N):
    a = random.randint(0,1)
    if(a ==0):
        initial_state.append(-1)
    else:
        initial_state.append(1)


# In[10]:


#Energy calculation function

def calculate_energy(state):
    energy = 0
    J = 1
    
    for i in range(N):
        energy += J * state[i-1] * state[i]
    
    return(energy)


# In[11]:


def change_in_energy(prev_state, state):
    diff = calculate_energy(state) - calculate_energy(prev_state)
    return(diff)


# In[12]:


def generate_state():
    initial_state = []

    for i in range(N):
        a = random.randint(0,1)
        if(a ==0):
            initial_state.append(-1)
        else:
            initial_state.append(1)
    return(initial_state)


# In[13]:


def correlation(state):
    minus = sum(state) / N
    
    correlated_sum = 0
    
    for i in range(N-1):
        correlated_sum += state[i] * state[i+1]
    
    return(correlated_sum/N - minus**2)


# In[16]:


M = 100
number_of_states = 100
ticks = []

T_initial = 0.1
increment = 0.1
average_correlations = []
temperatures = []


for j in range(number_of_states):
    state_j = generate_state()
    correlation_j = 0

    for i in range(M):
        candidate = random.randint(0, N-1)

        new_state = initial_state
        new_state[candidate] = new_state[candidate]*(-1)
        change = change_in_energy(initial_state, new_state)
        if(change <= 0):
            initial_state = new_state

        else:
            b = random.random()
            if(b <= e**(change/(1.38*(10**-23))/T_initial)):
                initial_state = new_state
        correlation_j += correlation(initial_state)
        ticks.append(i)
    
    average_correlations.append(correlation_j/N)
    
    temperatures.append(T_initial)
    T_initial += increment
    


    
    


# In[17]:


plt.plot(temperatures, average_correlations)


# In[ ]:




