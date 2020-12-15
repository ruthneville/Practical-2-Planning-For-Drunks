# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 13:00:15 2020

@author: Ruth Neville
"""
"""
Algorithm for the model:
    1. Set up the town
    2. Make the drunks and allocate them houses
    3. Move the drunks and track their steps in a density plot
    4. Save the density map to a txt file
    
"""
# Import libraries
import csv # import software to import csv files
import matplotlib.pyplot as mlp #import plotting software
from time import perf_counter # import software to count time 
import drunkframework # import the Drunk class

# Set up the drunks
# Create environment for drunks (the town for houses and the pub)
town = []
# create a list for drunks
drunks = []
# create a list for density
density = []
# Assign a number of drunks (tried with 1 for a test)
num_of_drunks = 25 
# Assign number of iterations - the more iterations the more likely they are to find their way home.
# It would be good to work out a method of getting them home without a set number of iterations?
num_of_iterations = 1000000


"""
1. SET UP THE ENVIRONMENT (TOWN)
"""

# Open CSV file
f = open(r'drunkplan.txt')

# Read in the environment (town)
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)
# Shift environment into a 2D list
for row in reader:
    rowlist = []
# Add each value to the rowlist
    for value in row:
        if value == 1:
            # change colour of pub so that it appears on the map
            rowlist.append(300)
        else:
            rowlist.append(value)
# Attach rowlist to environment
    town.append(rowlist)
# Close the file
f.close()

# Read in environment again to create a second list for density mapping
# Open CSV file
j = open(r'drunkplan.txt')

# Read in the environment (density)
reader = csv.reader(j, quoting = csv.QUOTE_NONNUMERIC)
# Shift environment into a 2D list
for row in reader:
    rowlist = []
# Add each value to the rowlist
    for value in row:
        if value == 1:
            # change colour of pub so that it appears on the map
            rowlist.append(300)
        else:
            rowlist.append(value)
# Attach rowlist to environment
    density.append(rowlist)
# Close the file
j.close()

#Show the environment to make sure it has been read in properly (TEST)
#mlp.imshow(town)
#mlp.show()

            
"""
2. MAKE THE DRUNKS AND GIVE THEM HOUSES
"""

# create drunks and add to environment
for i in range(num_of_drunks):
    # Python begins at 0 so add 1 and then times by 10 to get the house numbers 
    house = ((1+i)*10)
    # print(house) # TEST - are the houses correct?
    drunks.append(drunkframework.Drunk(density, drunks, house, town))

# Check the drunks are in the pub
#mlp.imshow(town)
#for i in range(num_of_drunks):
#    mlp.scatter(drunks[i].x, drunks[i].y)
#mlp.show()

# Start the clock to see how long it takes for the code to run (drunks to get home)
t1_start = perf_counter()

"""
# 3. MOVE THE DRUNKS AND DRAW THEIR MOVES TO TRACK DENSITY AND PLOT
"""

# print statement to show when the drunks arrive home
print("The following drunks have found their way home:\n")

# get the drunks to move if they are not at their house    
for i in range(num_of_drunks):
   drunk = drunks[i]
   for j in range(num_of_iterations):
        if town [drunk.y][drunk.x] != drunk.house: 
            drunks[i].walkhome()
            # why when i add density function do all the drunks move again???
            drunks[i].mark()
            if town [drunk.y][drunk.x] == drunk.house:
                print(f"{drunk.house} is Home!")
                
# Stop the clock when the drunks get home- could probably reduce the time with fewer iterations       
t1_stop = perf_counter()

# Plot the environment with the drunks and houses now the drunks have gone home
mlp.xlim(0,300) # Set the x axis to 0 - 300
mlp.ylim(0,300) # Set the y axis to 0 - 300
mlp.title("Final Model - Drunks Getting Home From the Pub")
mlp.ylabel("Town - Pub and Houses")
mlp.xlabel("Town - Pub and Houses")
# mlp.legend("Drunks", loc = "upper center")
mlp.imshow(density)  
for i in range(num_of_drunks):
    # drunks marked by small red triangles
    mlp.scatter(drunks[i].x, drunks[i].y, color="red", marker="^", s=40)   
# show the plot
mlp.show()

# Print the time for the drunks to get home
print(f"\nIt took the drunks {t1_stop - t1_start} seconds to get home!")
 

"""
 4. SAVE THE DENSITY MAP TO A TXT FILE
"""

# Write density text-file
# Save the density data as a text-file
with open('town.txt', 'w', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    # For each row in density list
    for row in density:
        # Write the row values into the density.txt file
        csvwriter.writerow(row)
