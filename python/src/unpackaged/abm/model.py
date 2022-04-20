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


'''
# Making agents

for i in range(num_of_agents): # the range value is defned in the num of agents varable
    agents.append([random.randint(0,100),random.randint(0,100)])# the iterations value is defned in the num of iterations varable
# Random movement of the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100



answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer)




# Plot on graph
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show() 

# Loop for extracting the distance for the 10 agents in relation to oneanother
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) '''
