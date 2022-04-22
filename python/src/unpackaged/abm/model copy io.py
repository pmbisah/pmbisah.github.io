"""
Agent Based Model
ABM
 Model program, containing variables representing two agents' locations 
 (y and x coordinates for each)
Created by 201566344

5th April 2022"""

import random # this random number generator will be used in step 3
import operator # this is required to calculate distance between agents later
import  matplotlib.pyplot # this is used to plot agents on a graph

import agentframework  # this imports tahe agentframwork.py class from the same directory as the model.py
import csv  # this is used to import csv file to read an external txt file

# function for distance calculation between agent to be used later in a loop
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x- agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10 
num_of_iterations =100
agents = []

"""
a = agentframework.Agent()
print(a.y, a.x)

a.move()
print(a.y, a.x)
"""
def __init__(self):
    self.environment = environment
    self.store = 0 # 
    
# Make agents based on num_agents variable
for i in range(num_of_agents):
    agents.append(agentframework.Agent())

# Move agents based on the num_of_iterations variable -loop
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)













f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader: # A list of rows
    for value in row: # A list of value
        print(value) # Floats
f.close()

environment = []
rowlist = []
environment.append(rowlist)
rowlist.append(value)

matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show() 