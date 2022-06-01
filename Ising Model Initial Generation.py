#!/usr/bin/env python
# coding: utf-8

# In[6]:


#create initial state
#write the energy calculation function
#flip one spin
#calcualte energy change
#...


# In[7]:


import random

import matplotlib.pyplot as plt

N = 1000


def generate_state():
    initial_state = []

    for i in range(N):
        a = random.randint(0,1)
        if(a ==0):
            initial_state.append(-1)
        else:
            initial_state.append(1)
    return(initial_state)


#create initial state

#N = 1000

#initial_state = []

#for i in range(N):
 #   a = random.randint(0,1)
  #  if(a ==0):
    #    initial_state.append(-1)
  #  else:
   #     initial_state.append(1)


# In[8]:


# what is the interaction type : en yakın komşu interaction'ları
def calculate_energy(state):
    energy = 0
    J = 1
    
    for i in range(N):
        energy += state[i-1] * state[i]
    
    return(energy)


# In[10]:


num_initial_states = 10000

states = []

for i in range(num_initial_states):

    b = random.randint(0,1)
    print(b)
    st = generate_state()
    states.append(calculate_energy(st))


# In[11]:


states


# In[14]:


fig = plt.figure()

plt.title("Ising model")

plt.xlabel("Initial state")
plt.ylabel("energy")

plt.xlim([0, num_initial_states])

plt.ylim([-1000, 1000])


# In[16]:


xaxis = []


for h in range(num_initial_states):
    xaxis.append(h)


# In[17]:


plt.plot(xaxis, states)


# In[ ]:




