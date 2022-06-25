"""
Author:  Anuj Gautam
"""

from visualise import show_vegetation_type
from visualise import show_vegetation_density
from visualise import show_wind_speed
from visualise import show_bushfire
from visualise import show_fire_risk

import csv
import math
import random


def load_vegetation_type(filename):
    '''
    Reads a comma separated values (csv) file 
    and returns the data as a list of lists.
    Blank value  is read as an empty string ''.
    --------
    << Parameters >>
    filename : (str) Filename or path of the csv file to be read

    << Returns >>
    data : (list of lists of str elements) 
    '''
    with open(filename) as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data
        
def load_vegetation_density(filename):
    '''
    Reads a comma separated values (csv) file 
    and returns the data as a list of lists.
    Blank value is read as 0.0 .
    --------
    << Parameters >>
    filename : (str) Filename or path of the csv file to be read

    << Returns >>
    data : (list of lists of float elements)
    '''
    with open(filename) as file:
        reader = csv.reader(file)
        data = [row for row in reader]
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == '':        #Convert blank values to 0.0
                    data[i][j] = 0.00
                else:
                    data[i][j] = float(data[i][j])
    return data

def load_wind_speed(filename):
    '''
    Reads a comma separated values (csv) file 
    and returns the data as a list of lists.
    Blank value is read as 0.0 .
    --------
    << Parameters >>
    filename : (str) Filename or path of the csv file to be read

    << Returns >>
    data : (list of lists of float elements)
    '''
    with open(filename) as file:
        reader = csv.reader(file)
        data = [row for row in reader]
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == '':        #Convert blank values to 0.0
                    data[i][j] = 0.0
                else:
                    data[i][j] = float(data[i][j])
    return data

def load_bushfire(filename):
    '''
    Reads a comma separated values (csv) file 
    and returns the data as a list of lists.
    Blank value is read as -1.
    --------
    << Parameters >>
    filename : (str) Filename or path of the csv file to be read

    << Returns >>
    data : (list of lists of int elements)
    '''
    with open(filename) as file:
        reader = csv.reader(file)
        data = [row for row in reader]
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == '':
                    data[i][j] = -1     #Convert blank values to -1
                else:
                    data[i][j] = int(data[i][j])
    return data



# The argument to this function is a wind speed map, in the
# form of a list of lists; it is the same data structure that
# is returned by your implementation of the load_wind_speed
# function.

def highest_wind_speed(wind_speed):
    '''
    Returns the highest wind speed in the windspeed map.
    --------
    << Parameters >>
    wind_speed: (list of lists of float elements) Map of wind speeds
    
    << Returns >>
    out : (float) Maximum wind speed
    '''
    return max([max(sublist) for sublist in wind_speed])


# The argument to this function is a vegetation type map, in the
# form of a list of lists; it is the same data structure that
# is returned by your implementation of the load_vegetation_type
# function.

def count_cells(vegetation_type):
    '''
    Prints the number of cells covered by each vegetation type.
    ---------
    << Parameter >>
    vegetation_type: (list of lists of str elements) Map of different 
                    vegetation types

    << Retrurns >>
    No return statements: (NoneType)
    '''

    type_and_count = {}
    for row in vegetation_type:
        for vege in row:
            if vege=='':
                continue
            else:
                if vege in type_and_count:
                   type_and_count[vege] += 1
                else:
                   type_and_count[vege] = 1

    for item in type_and_count:
        print(item+':', type_and_count[item])
    


# The arguments to this function are a vegetation type map and
# a vegetation density map, both in the form of a list of lists.
# They are the same data structure that is returned by your
# implementations of the load_vegetation_type and load_vegetation_density
# functions, respectively.

def count_area(vegetation_type, vegetation_density):
    '''
    Prints the area covered by each vegetation type.
    ---------
    << Parameter >>
    vegetation_type: (list of lists of str elements) Map of different 
                    vegetation types
    vegetation_density: (list of lists of float elements) Map of vegetation
                        density at each cell

    << Retrurns >>
    No return statements: (NoneType)
    '''

    type_and_density={}
    for i in range(len(vegetation_type)):
        for j in range(len(vegetation_type[i])):
            if vegetation_type[i][j]=='':
                continue
            else:
                if vegetation_type[i][j] in type_and_density:
                    type_and_density[vegetation_type[i][j]] += vegetation_density[i][j]*1e4
                else:
                    type_and_density[vegetation_type[i][j]] = vegetation_density[i][j]*1e4
    for item in type_and_density:
        print(item+':',"%.2f"%type_and_density[item],'sq m')


# The arguments to this function are:
# x and y - integers, representing a position in the grid;
# vegetation_type - a vegetation type map (as returned by your
#   implementation of the load_vegetation_type function);
# vegetation_density - a vegetation density map (as returned by
#   your implementation of the load_vegetation_density function);
# wind_speed - a wind speed map (as returned by your implementation
#   of the load_wind_speed function).
def fire_risk_factor(i, j, vegetation_density, vegetation_type):
    '''
    Returns the risk factor for different vegetation types.
    ---------
    << Parameter >>
    i: (int) Row index
    j: (int) Column index
    vegetation_type: (list of lists of str elements) Map of different 
                    vegetation types
    vegetation_density: (list of lists of float elements) Map of vegetation
                        density at each cell

    << Retrurns >>
    (float) Risk factor
    '''
    if vegetation_type[i][j]=='Shrubland' or vegetation_type[i][j]=='Pine Forest':
        a = 0.2
    elif vegetation_type[i][j]=='Arboretum':
        a = 0.1
    elif vegetation_type[i][j]=='Urban Vegetation' or vegetation_type[i][j]=='Golf Course':
        a = 0.05
    else:
        a = 0
    return math.sqrt(a+vegetation_density[i][j])

def beyond_edge(i, j, any_map):
    '''
    Returns True if the index (i, j) is beyond the edge of vegetation density map.
    Else returns False. 
    ---------
    << Parameter >>
    i: (int) Row index
    j: (int) Column index
    any_map: (list of lists) Map

    << Retrurns >>
    (bool)
    '''
    if i < 0 or j < 0 or i>=len(any_map) or j>=len(any_map[i]):                 #Boundary check
        return True
    else:
        return False
    
def fire_risk(x, y, vegetation_type, vegetation_density, wind_speed):
    '''
    Returns the fire risk for a particular cell.
    ---------
    << Parameter >>
    x: (int) Column index (East to West)
    y: (int) Row index (North to South)
    vegetation_type: (list of lists of str elements) Map of different 
                    vegetation types
    vegetation_density: (list of lists of float elements) Map of vegetation
                        density at each cell
    wind_speed: (list of lists of float elements) Map of wind speeds 
                at each cell

    << Retrurns >>
    (float) Fire risk
    '''

    n = math.floor(wind_speed[y][x])
    risk = 0
    for j in range(y - (n-1), y + n):           #Iterating over nearby cells
        for i in range(x - (n-1), x + n):       #that are less than floor(n) distance away
            if beyond_edge(j, i, vegetation_density) == False:                          #Check if beoynd edge
                risk += fire_risk_factor(j, i, vegetation_density, vegetation_type)     #Add nearby fire risk factors
    return risk


# The arguments to this function are an initial bushfile map (a list
# of lists, as returned by your implementation of the load_bushfire
# function), a vegetation type map (as returned by your implementation
# of the load_vegetation_type function), a vegetation density map (as
# returned by your implementation of load_vegetation_density) and a
# positive integer, representing the number of steps to simulate.
def convert_bushfire_type(bushfire_map, to_type):
    '''
    Returns bool or int bushfire map. Used for coversion between 
    bool and int datatypes.
    ---------
    << Parameter >>
    bushfire_map: (list of list of bool or int elements 
    totype: (str) "int" or "bool"

    << Retrurns >>
    bushfire_map: (list of list of bool or int elements)
    '''
    if to_type == "int":                                # To change the empty None element to -1, easy for calculations
        for l in range(len(bushfire_map)):                          
            for m in range(len(bushfire_map[l])):
                if bushfire_map[l][m] == True:
                    bushfire_map[l][m]= 1
                elif bushfire_map[l][m] == False:
                    bushfire_map[l][m] = 0
                elif bushfire_map[l][m] == None:
                    bushfire_map[l][m] = -1

    elif to_type == "bool":                             # To change the empty -1 element to None and calculated (>0) integers to bool, easy when using imshow
        for l in range(len(bushfire_map)):
            for m in range(len(bushfire_map[l])):
                if bushfire_map[l][m] > 0:
                    bushfire_map[l][m] = True
                elif bushfire_map[l][m] == 0:
                    bushfire_map[l][m] = False
                elif bushfire_map[l][m] == -1:
                    bushfire_map[l][m] = None
    
    return bushfire_map


def spread_cell(bushfire_map, steps, stochastic, risk):
    '''
    Returns the simulated spread bushfire after 'n' number of steps.
    ---------
    << Parameter >>
    bushfire_map: (list of lists of float elements) Map of the bushfire
    steps: (int) Simulation steps 
    stochastic: (bool) Stochastic simulation (True) or not (False)
    risk: (list of lists of float elements) Map of the risk
            of each cell catching fire (pass only if stochastic == True, else [])

    << Retrurns >>
    bushfire_map: (list of lists of float elements) Map of the spread bushfire 
    '''
    
    bushfire_map = convert_bushfire_type(bushfire_map, "int")       #Only used in Q8, to convert the bool bushfire map to int bushfire map

    for step in range(1, steps+1):
        for i in range(len(bushfire_map)):
            for j in range( len(bushfire_map[i]) ):
                if 0 < bushfire_map[i][j] <= step  :                     
                    for x in range(i-1, i+2):           # Iterating over surrounding
                        for y in range(j-1, j+2):       # 8 cells and itself
                            if stochastic == True:      # Stochastic simulation (Q7) 
                                if beyond_edge( x, y, bushfire_map ) == False:      
                                    if bushfire_map[x][y] == 0 and risk[x][y] > random.random():    # Compare normalized fire risk with a random number [0, 1) 
                                        bushfire_map[x][y] = step + 1                                  # Give the step number to the newly lit cell to signify fire spread
                            
                            else:                       # Non-stochastic simulation (Q5)  
                                if beyond_edge( x, y, bushfire_map ) == False:
                                    if bushfire_map[x][y] == 0:
                                        bushfire_map[x][y] = step + 1                                 # Give the step number to the newly lit cell to signify fire spread

    #Convert the integer bushfire map to bool bushfire map which is read by show_bushfire()
    bushfire_map = convert_bushfire_type(bushfire_map, "bool")
    
    return bushfire_map


def simulate_bushfire(initial_bushfire, vegetation_type, vegetation_density, steps):
    '''
    Returns the spread bushfire after 'n' number of steps.
    ---------
    << Parameter >>
    initial_bushfire: (list of lists of float elements) Map of the initial bushfire
    vegetation_type: (list of lists of str elements) Map of different 
                    vegetation types
    vegetation_density: (list of lists of float elements) Map of vegetation
                        density at each cell
    steps: (int) Simulation steps 

    << Retrurns >>
    bushfire_map: (list of lists of bool elements) Map of the spread bushfire 
    '''
    
    bushfire_map = spread_cell(initial_bushfire, steps, False, [] ) # False: Non-stochastics imulation, []: no risk factor map needs to be passed

    return bushfire_map

            




# The arguments to this function are two bushfile maps (each a list
# of lists, i.e., same format as returned by your implementation of
# # the load_bushfire function).

def compare_bushfires(bushfire_a, bushfire_b):
    '''
    Returns the percentage of same cells between two bushfire maps.
    ---------
    << Parameter >>
    bushfire_a: (list of lists of float elements) Map of bushfire a
    bushfire_b: (list of lists of float elements) Map of bushfire b

    << Retrurns >>
    percentage: (float) Percentage of same cells
    '''
    same_cells = 0
    total_cells = 0
    
    bushfire_a = convert_bushfire_type(bushfire_a, "int")               # Converting possible bool bushfire map type to integer for later comparison
    bushfire_b = convert_bushfire_type(bushfire_b, "int")               # Converting possible bool bushfire map type to integer for later comparison

    for i in range( len(bushfire_a)):
        total_cells += len(bushfire_a[i]) - bushfire_a[i].count(-1)     # total filled up cells in a row : (length - number of empty cells)
        for j in range( len(bushfire_a[i])):
                if bushfire_a[i][j] == bushfire_b[i][j] and bushfire_b[i][j] != -1 :
                    same_cells += 1
                
    percentage = (same_cells / total_cells)
    return percentage

# The arguments to this function are:
# initial_bushfire - an initial bushfile map (a list of lists, same
#   as returned by your implementation of the load_bushfire function);
# steps - a positive integer, the number of steps to simulate;
# vegetation_type - a vegetation type map (as returned by your
#   implementation of the load_vegetation_type function);
# vegetation_density - a vegetation density map (as returned by
#   your implementation of the load_vegetation_density function);
# wind_speed - a wind speed map (as returned by your implementation
#   of the load_wind_speed function).

def simulate_bushfire_stochastic(initial_bushfire, steps,
    vegetation_type, vegetation_density, 
    wind_speed):
    '''
    Returns the spread bushfire after 'n' number of steps. Stochastic simulation.
    ---------
    << Parameter >>
    initial_bushfire: (list of lists of integer elements) Map of the initial bushfire
    steps: (int) Simulation steps 
    vegetation_type: (list of lists of str elements) Map of different 
                    vegetation types
    vegetation_density: (list of lists of float elements) Map of vegetation
                        density at each cell
    wind_speed: (list of lists of float elements) Map of wind speeds 
                at each cell

    << Retrurns >>
    bushfire_map: (list of lists of bool elements) Map of the spread bushfire 
    '''
    
    risk = [[] for i in range( len(initial_bushfire) )]

    # get the fire risk map
    for i in range(len(initial_bushfire)):
        for j in range(len(initial_bushfire[i])):
            risk[i].append(fire_risk(j, i, vegetation_type, vegetation_density, wind_speed))
    

    max_risk = max([max(sublist) for sublist in risk])

    for i in range(len(initial_bushfire)):
        for j in range(len(initial_bushfire[i])):
            risk[i][j] = risk[i][j] / max_risk  # normalise risk
    
    bushfire_map = spread_cell(initial_bushfire, steps, True, risk)

    return bushfire_map

                

if __name__ == '__main__':
    pass
