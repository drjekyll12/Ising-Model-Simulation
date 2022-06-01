#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Imports 

import random
import matplotlib.pyplot as plt
from math import e




# In[2]:


N = 10000 #number of spins

initial_state = []

for i in range(N):
    a = random.randint(0,1)
    if(a ==0):
        initial_state.append(-1)
    else:
        initial_state.append(1)


# In[3]:


#Energy calculation function

def calculate_energy(state):
    energy = 0
    J = 1
    
    for i in range(N):
        energy += J * state[i-1] * state[i]
    
    return(energy)


# In[4]:


def change_in_energy(prev_state, state):
    diff = calculate_energy(state) - calculate_energy(prev_state)
    return(diff)


# In[5]:


def generate_state():
    initial_state = []

    for i in range(N):
        a = random.randint(0,1)
        if(a ==0):
            initial_state.append(-1)
        else:
            initial_state.append(1)
    return(initial_state)


# In[6]:


M = 100
number_of_states = 1000
ticks = []

T_initial = 0.1
increment = 0.1
magnetizations = []
temperatures = []


for j in range(number_of_states):
    state_j = generate_state()
    magnetization = 0

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
        magnetization += sum(initial_state)
        ticks.append(i)
    
    magnetizations.append(magnetization/N)
    
    temperatures.append(T_initial)
    T_initial += increment
    


# In[7]:


plt.plot(temperatures, magnetizations)


# In[ ]:




