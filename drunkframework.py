 # -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 13:41:00 2020

@author: Ruth Neville
"""
# import random number genertor
import random

# Set random number to be same every time the model is run 
random.seed(1)

class Drunk:
 """An attempt to model a drunk."""
 def __init__ (self, density, drunks, house, town): 
        """Initalise starting location and home attributes."""
        self.drunks = drunks 
        self.town = town 
        self.house = house
        self.density = density
        """All walks start at (137,158) """
        self.x = 137 
        self.y = 158 
        
        
 def walkhome(self): 
         """Simulate a random walk.
         Parameters
         ----------
         x: number
         This is what is either added or taken from
         
         Returns
         -------
         x: number plus or minus 1.
         """
        
         if random.random() < 0.5: 
            self.y = (self.y + 1) % 300 
         else: 
            self.y = (self.y - 1) % 300 
       
         if random.random() < 0.5: 
            self.x = (self.x + 1) % 300 
         else: 
            self.x = (self.x - 1) % 300  
            
    
 def mark(self):
        """Mark the density of steps taken by each drunk."""
        self.density[self.y][self.x] += 1