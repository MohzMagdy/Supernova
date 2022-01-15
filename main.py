from vpython import *
from rate import *
from files import *
from console import *   
from phys import *
from buttons import *

while True:
    rate(30)
    diff_data = [] # List of dictionaries with planet difference in position and momentum
    for planet in planets_list:
        diff_data.append({
            'pos': vector(0,0,0),
            'p': vector(0,0,0)
        })

    for i in range(len(planets_list)-1):
        for j in range(i+1, len(planets_list)):
            motion = move_planet(planets_list[i], planets_list[j])     
            diff_data[i]['pos'] += motion[0][0] - planets_list[i].pos
            diff_data[i]['p'] += motion[0][1] - planets_list[i].p
            diff_data[j]['pos'] += motion[1][0] - planets_list[j].pos
            diff_data[j]['p'] += motion[1][1] - planets_list[j].p

    for i in range(len(planets_list)):
        planets_list[i].pos += diff_data[i]['pos']
        planets_list[i].p += diff_data[i]['p']

#scene.range = 20
#if True:
    # k = keysdown() # a list of keys that are down
    # if 'down' in k: rate = 10000
    # if 'up' in k: rate = 10
