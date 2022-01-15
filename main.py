from vpython import *
from rate import *
from files import *
from console import *   
from phys import *
from buttons import *

# Main loop
while True:
    rate(30)

    # List of dictionaries with planet difference in position and momentum
    diff_data = [] 
    for planet in planets_list:
        diff_data.append({
            'pos': vector(0,0,0),
            'p': vector(0,0,0)
        })

    # Calculates change in position and momentum of each planet due to effect of each other planet
    for i in range(len(planets_list)-1): 
        for j in range(i+1, len(planets_list)):
            motion = move_planet(planets_list[i], planets_list[j])     
            diff_data[i]['pos'] += motion[0][0] - planets_list[i].pos
            diff_data[i]['p'] += motion[0][1] - planets_list[i].p
            diff_data[j]['pos'] += motion[1][0] - planets_list[j].pos
            diff_data[j]['p'] += motion[1][1] - planets_list[j].p

    # Changes the position and momentum of each planet according to the difference calculated
    for i in range(len(planets_list)):
        planets_list[i].pos += diff_data[i]['pos']
        planets_list[i].p += diff_data[i]['p']
