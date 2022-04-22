"""
Agent Based Model
ABM
 Model program, containing variables representing two agents' locations 
 (y and x coordinates for each)
Created by 201566344

5th April 2022"""

import random # this random number will be used for the agentframework module
import operator # this is required to calculate distance between agents later
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot # this is used to plot agents on a graph
import matplotlib.animation 
import agentframework  # this imports tahe agentframwork.py class from the same directory as the model.py
import csv  # this is used to import csv file to read an external txt file


# SET PARAMETERS THE PARAMETERS CAN BE CHANGE HERE
num_of_agents = 10      #Number of Agents
num_of_iterations =100  #Number of Iterations
neighbourhood = 20      #Numer of Neighborhoods
environment = []        # Crates an empty list 
agents = []             # Crates an empty list 


"""
a = agentframework.Agent()
print(a.y, a.x)

a.move()
print(a.y, a.x)
"""
# Reading a text file and placing it into an enviroment              
f = open('in.txt', newline='')      #read the text a line at a time
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) #convert to float
for row in reader:				     #reading in the rows a row at a time
    rowlist = []                    
    for value in row:
        rowlist.append(value) 
    environment.append(rowlist)       # placing it into the evoronment
f.close()


# Make agents based on num_agents variable in relation to the environment
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

"""
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

"""
# Ploting the agents in the envronment         
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

#  a loop for moving the agent eat and sharing points with neighbours

for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)


