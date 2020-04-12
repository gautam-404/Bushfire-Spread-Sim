"""
Author: Anuj Gautam
Date: 21/10/18
"""

import assignment as asst
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def count_burning_veg_type(bushfire_map, vegetation_type, veg_dict, step):
    '''
    Prints the number of cells of each vegetation type on fire .
    ---------
    << Parameter >>
    bushfire_map: (list of lists) bushfire map
    vegetation_type: (list of lists of str elements) Map of different 
                    vegetation types
    veg_dict: (dict of lists) each list contains count of vegeration
                         types on fire and different steps
    step: (int) n^th step

    << Retrurns >>
    veg_dict: (dict of lists) each list contains count of vegeration
                         types on fire and different steps
    '''
    type_and_count = {'Total':0}
    #counting the number of cells of each vegetation type on fire
    for i in range(len(vegetation_type)):
        for j in range(len(vegetation_type[i])):
            if vegetation_type[i][j] == '':
                continue
            else:
                if vegetation_type[i][j] in type_and_count and bushfire_map[i][j] == True:
                    type_and_count[vegetation_type[i][j]] += 1
                elif vegetation_type[i][j] not in type_and_count and bushfire_map[i][j] == True:
                    type_and_count[vegetation_type[i][j]]  = 1
                elif vegetation_type[i][j] not in type_and_count and bushfire_map[i][j] == False:
                    type_and_count[vegetation_type[i][j]] = 0

    type_and_count['Total'] += sum(type_and_count.values()) - type_and_count['Total']       #total cells on fire
    
    # creating a list of cells on fire for each vegetation type and total, index represents step
    for key, item in type_and_count.items():
        if step == 0:
            veg_dict[key] = [item]
        else:
            veg_dict[key].append(item)

    
    return veg_dict

def plot_linked_scatter(steps, veg_dict):
    '''
    Plots the total number of cells of different 
    vegetation tyes on fire at different times.
    ---------
    << Parameter >>
    veg_dict: (dict of lists) each list contains count of vegeration
                         types on fire and different steps
    steps: (int) total steps

    << Retrurns >>
    --------------
    '''
    t = range(0, steps +2)  
    
    plt.figure( figsize = (15,12) )
    for key, item in veg_dict.items():
        plt.plot(t, item, marker = 'o', label = (key+": %i" %item[steps]), markersize = 0.5 )
        plt.xlabel("$ t_0 \ + \  %i \Delta \ t $" %(steps) )
        plt.ylabel("Number of cells on fire")
        plt.legend()
    plt.show()



def plot_fire_spread(initial_bushfire, vegetation_type, vegetation_density, wind_speed):
    '''
    Plots the number of cells on fire over time for each vegetation type.
    ---------
    << Parameter >>
    initial_bushfire: (list of lists of float elements) Map of the initial bushfire
    vegetation_type: (list of lists of str elements) Map of different 
                    vegetation types
    vegetation_density: (list of lists of float elements) Map of vegetation
                        density at each cell
    wind_speed: (list of lists of float elements) Map of wind speeds 
                at each cell

    << Retrurns >>
    --------------
    '''
    
    risk = [[] for i in range( len(initial_bushfire) )]
    # get the fire risk map
    for i in range(len(initial_bushfire)):
        for j in range(len(initial_bushfire[i])):
            risk[i].append(asst.fire_risk(j, i, vegetation_type, vegetation_density, wind_speed))
    
    max_risk = max([max(sublist) for sublist in risk])
    for i in range(len(initial_bushfire)):
        for j in range(len(initial_bushfire[i])):
            risk[i][j] = risk[i][j] / max_risk  # normalise risk
    
    steps = 700
    bushfire_map = initial_bushfire.copy()
    veg_dict = {}
    for step in range(0, steps+2):
        veg_dict = count_burning_veg_type( bushfire_map, vegetation_type, veg_dict, step )      # number of cells on fire over time for each vegetation type after each step
        bushfire_map = asst.spread_cell(bushfire_map, 1, True, risk )                           # spreading fire to nearby cells with stochastic = True
        
        # bushfire_map = asst.simulate_bushfire_stochastic(bushfire_map, 1,                     #Alternate way, but slower (calculates fire risk everytime the fn is called)
        #                             vegetation_type, vegetation_density,
        #                             wind_speed)
    
    plot_linked_scatter(steps, veg_dict)

if __name__ == '__main__':
    pass
