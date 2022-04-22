# -*- coding: utf-8 -*-
'''
Agent Based Model: Agent


Created by 201566344


15th April 2022'''
import random 

class Agent: # Creating class

    def __init__ (self, environment, agents):  
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)     
        self.environment = environment  #setting environment
        self.agents = agents            #setting agents
        self.store = 0 

   
    def move(self):    # Method to to move Y and X
        if random.random() < 0.5:
           self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
       
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
    
    def eat(self):
        if  self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10 
 