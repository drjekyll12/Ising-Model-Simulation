# Ising-Model-Simulation
AP CS A final project. The project is based on the simulation of a d=1 Ising model with spin values +-1. 

# The Ising Model

Just like any other mathematical model, the Ising model is a model constructed to conveniently investigate real-world behavior of different systems. These real-world situations could range from the thermodynamic analysis of water to the analysis of a quantum electrodynamic system, or even to the investigation of a biological system.

The Ising model is a relatively simple model, consisting of sites, generally called “spins”, that can take a variety of values depending on the definition of the system. The simplest version of the Ising model is the one where the spins can take one of the two values: -1 or +1. In technical terms, this refers to the fact that each spin i has the value si (sometimes shown as 𝞂i) that can be either -1 or +1. These sites are arranged in a lattice configuration that have d dimensions, and d=1 generates the simplest Ising model system, a string of spins.

<p align="center">
  <img src="images/ising%20model.png" />
</p>

However, the Ising model does not govern systems with all numbers of sites, it specifically requires the site number to be infinite which is the most important feature of the model that allows the system to be solved, either definitely or via approximations. Therefore, i=1,2,3, ... , N where N tends to infinity. 

Alongside these, the Ising model is not bounded by the fact that si= ±1. si can take a variety of values, discrete or continuous as in Heisenberg models or spin glasses.

Although the Ising model possesses aspects regarding many macroscopic values, the main component of every system is the total energy of the system and how it is calculated. In the Ising model, depending on how many types of interactions or individual factors the model has, the Hamiltonian can be written as such, in the most basic form:

<p align="center">
  <img src="images/hamiltonian.png" />
</p>


Similarly, a statistical concept that will be useful in the future sections is the partition function, given by Z. The partition function is defined as:

<p align="center">
  <img src="images/partition%20function.png" />
</p>

# Renormalization Group and Kadanoff’s Approach: The Big Idea
Philosophically, Kadanoff’s approach to the Ising model as well as Ken Wilson’s groundbreaking interpretation of Kadanoff’s method changed the science world. Even though the idea behind these theories was simple, it had made a huge impact on how a problem was viewed and tackled. Instead of using mean-field approaches, the system was rescaled. Instead of trying to solve a system with infinite particles, a system that has fewer but still infinite number of particles was solved. Through this iterative approach, Ken Wilson soon figured out a way to completely separate the rescaled system and make it a copy of the initial one in terms of macroscopic behavior. The method and the calculations behind the method will be discussed later on in this research paper.

# Graphs Created and Explanations

## Energy vs Ticks

The "Energy vs Ticks" graph is generated using the code block that can be found in the "Energy vs Ticks.py" file. After a random initial state has been created, utilizing the Metropolis algorithm, the evolution of that particular Ising model system can be observed. However, the "Energy vs Ticks" graph gives insight as to how the total energy of the system is changing as the system evolves. The temperature value and how many times the simulation is run can be changed to obtain various results. 

<p align="center">
  <img src="images/energy%20vs%20ticks%20graph.png" />
</p>

Following the laws of physics, it is expected for the system to decrease in total energy as the system evolves, which is what occurs as seen in the image above.

## Average Correlation Length vs Ticks

To give a general idea of how the correlation length of the Ising system changes over ticks, the average length of blocks of +1 or -1 spins are calculated for each state. As the system is updated this value changes. This is a significant oberservation in terms of how the simulation works since it allows us to see whether the system undergoes drastic changes in this frame of reference, and the stability observed here suggests better statistical results for other graphs. One of the graphs obtained is given below.

<p align="center">
  <img src="images/avg%20corr%20length%20vs%20ticks.png" />
</p>

Clearly, as the states are updated the correlation lengths converge to 1, that is the system is almost in the form +1,-1,+1,-1,..., which correlates with the "Energy vs Ticks" graph given above.

## Correlation vs Temperature

Here, the correlation of the system as the system is changing temperature measured using the correlation function given below. The correlation function yields how much correlation (non-randomness) is within the system.

<p align="center">
  <img src="images/correlation%20function.png" />
</p>

How the correlation of the system changes with temperature is important in terms of finding more about the critical temperature of the system. The graph generated using the correlation function and the temerpature that corresponded to that state is given below:

<p align="center">
  <img src="images/corr%20vs%20temp.png" />
</p>

## Magnetization vs Temperature

The magnetization of the system is given by the simple equation below:

<p align="center">
  <img src="images/magnetization%20equation.png" />
</p>

How the magnetization of the system changes with temperature is essential since it reveals what the critical temperature is. For d=1, spin=+-1 Ising systems after the critical temperature magnetization drops to 0 (which once again correlates with the results found in the "Average Correlation Length vs Ticks" section). This phenomenon canbe seen in the following phase diagram.

<p align="center">
  <img src="images/mag%20vs%20t%20%20phase%20diagram.png" />
</p>

