from vpython import *
from rate import *
from files import *
from console import *   
from phys import *

new_planets = [] # Imported planets not shown on screen and not in planets_data
planets_data = []

# Import and Export buttons
def console_import():
    global new_planets
    new_planets.append(from_console())
button(bind = console_import, text = 'Console Import')

def console_export():
    global planets_data
    to_console(planets_data)
button(bind = console_export, text = 'Console Export')

def file_import():
    global new_planets
    new_planets.extend(from_file(input('Enter file Path: ')))
button(bind = file_import, text = 'File Import')

def file_export():
    global planets_data
    to_file(input('Enter file Path: '), planets_data)
button(bind = file_export, text = 'File Export')

# headers = ['ID', 'Mass', 'Velocity', 'Temperature', 'Position'] #Add: Radius, optional texture
planets_list = []
def make_planets(uncreated_planets):
    global planets_list, planets_data, new_planets

    for planet_data in uncreated_planets:
        planet = sphere(id = planet_data['id'], 
        mass = planet_data['mass'], 
        vel = vector(planet_data['vel'][0], planet_data['vel'][1], planet_data['vel'][2]),
        temp = planet_data['temp'],
        pos = vector(planet_data['pos'][0], planet_data['pos'][1],planet_data['pos'][2]),
        radius = 0.2, p = vector(0,0,0), make_Trail = True)
        planet.p = planet.mass * planet.vel
        
        planets_list.append(planet)
        planets_data.append(planet_data)
        
button(bind = lambda: make_planets(new_planets), text = 'Make planets') #Using anonymous lambda function to give parameters

#For testing
def clear_planets():
    global new_planets
    new_planets.clear()
button(bind = clear_planets, text = 'Clear planets')



#scene.bind('click', Dec_Rate)
button( bind=start, text='Start!')
button( bind=Inc_Rate, text='Increase Rate!')
button( bind=Dec_Rate, text='Decrease Rate!')


sun = sphere(id = 1, pos=vector(0,0,0), radius = 0.8
             ,texture="https://media.istockphoto.com/photos/realistic-sun-or-star-closeup-3d-rendering-illustration-picture-id1267178422?b=1&k=20&m=1267178422&s=170667a&w=0&h=EtPtCIh3MP5f2f9XjNxTHChncLA5WUeuY5TWVuP1SEs=",
             mass = 1500 , p = vector(0,0,0))
p1 = sphere(id = 2, pos= vector(2,0,0), radius = 0.2, mass=1, p = vector(0,30,0), texture = "https://upload.wikimedia.org/wikipedia/commons/6/60/Earth_from_Space.jpg")

planets_list.append(sun)
planets_list.append(p1)

dt = 0.0001
while True:
    #rate(50)
    if start:
        rate(60)
        diff_data = [] # List of dictionaries with planet id and difference in position and momentum
        for planet in planets_list:
            diff_data.append({
                'pos': vector(0,0,0),
                'p': vector(0,0,0)})

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

    if Inc_Rate:
        rate(1000)
        motion = move_planet(p1, sun)
        p1.pos = motion[0][0]
        p1.p = motion[0][1]
        sun.pos = motion[1][0]
        sun.p = motion[1][1]
    if Dec_Rate:
        rate(10)
        motion = move_planet(p1, sun)
        p1.pos = motion[0][0]
        p1.p = motion[0][1]
        sun.pos = motion[1][0]
        sun.p = motion[1][1]


#scene.range = 20
#if True:
    k = keysdown() # a list of keys that are down
    if 'down' in k: rate = 10000
    if 'up' in k: rate = 10
