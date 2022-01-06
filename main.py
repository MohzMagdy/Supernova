from vpython import *
from rate import *
from files import *
from console import *   

global planets_data 
planets_data = []

# Import and Export buttons
def console_import():
    global planets_data
    planets_data.append(from_console())
button(bind = console_import, text = 'Console Import')

def console_export():
    global planets_data
    to_console(planets_data)
button(bind = console_export, text = 'Console Export')

def file_import():
    global planets_data
    planets_data.extend(from_file(input('Enter file Path: ')))
button(bind = file_import, text = 'File Import')

def file_export():
    global planets_data
    to_file(input('Enter file Path: '), planets_data)
button(bind = file_export, text = 'File Export')

# headers = ['ID', 'Mass', 'Velocity', 'Temperature', 'Position'] #Add: Radius, optional texture
global planets_list
planets_list = []

def make_planets(planets_data):
    global planets_list

    for planet_data in planets_data:
        planet = sphere(id = planet_data['id'], 
        mass = planet_data['mass'], 
        vel = vector(planets_data['vel'][0],planets_data['vel'][1], planets_data['vel'][2]),
        temp = planets_data['temp'],
        pos = vector(planets_data['pos'][0],planets_data['pos'][1],planets_data['pos'][2]),
        radius = 0.2, p = vector(0,0,0), make_Trail = True)
        planet.p = planet.mass * planet.vel
        
        planets_list.append(planet)
        planets_data = []
# button(bind = make_planets(planets_data), text = 'Make planets')



start = True
Dec_Rate = False
Inc_Rate = False
def start(b):
    #while rate() == 1:
    global start, Inc_Rate, Dec_Rate
    start = not start
    Dec_Rate = False
    Inc_Rate = False
    return start, Inc_Rate, Dec_Rate
#Start = Start and Start
def Inc_Rate(I):
    #while rate() == 500 or rate()==1:
    global start, Inc_Rate, Dec_Rate
    Inc_Rate = not Inc_Rate
    start = False
    Dec_Rate = False
    return start, Inc_Rate, Dec_Rate
def Dec_Rate():
    #while rate() == 1000 or rate()== 500:
    global start, Inc_Rate, Dec_Rate
    Dec_Rate = not Dec_Rate
    start = False
    Inc_Rate = False
    return start, Inc_Rate, Dec_Rate

#scene.bind('click', Dec_Rate)
button( bind=start, text='Start!')
button( bind=Inc_Rate, text='Increase Rate!')
button( bind=Dec_Rate, text='Decrease Rate!')


def calc_force(planet1, planet2):
    G = 1
    Distance_vector = planet1.pos - planet2.pos
    rhat = Distance_vector / mag(Distance_vector)
    force = -G * planet1.mass * planet2.mass / (mag(Distance_vector))**2 
    force_vector = force * rhat
    return force_vector



sun = sphere(pos=vector(0,0,0), radius = 0.8
             ,texture="https://media.istockphoto.com/photos/realistic-sun-or-star-closeup-3d-rendering-illustration-picture-id1267178422?b=1&k=20&m=1267178422&s=170667a&w=0&h=EtPtCIh3MP5f2f9XjNxTHChncLA5WUeuY5TWVuP1SEs=",
             mass = 1500 , p = vector(0,0,0), make_Trail = True)
#sun.p = vector(0,0,5) # Sphere angular momentum
planet1 = sphere(pos= vector(2,0,0), radius = 0.2, mass=1, p = vector(0,30,0), make_Trail = True
                 ,texture = "https://upload.wikimedia.org/wikipedia/commons/6/60/Earth_from_Space.jpg")
#planet1.mass = 100
#planet1.p = vector(0, 0, 5)
dt = 0.0001
t = 0
while True:
    #rate(50)
    if start:
        rate(300)
        sun.force = calc_force(sun, planet1)
        planet1.force = calc_force(planet1, sun)
        print(planet1.force)
        sun.p = sun.p + sun.force * dt
        planet1.p = planet1.p + planet1.force*dt
        sun.pos = sun.pos + sun.p / sun.mass*dt
        planet1.pos = planet1.pos + planet1.p / planet1.mass*dt
    if Inc_Rate:
        rate(1000)
        sun.force = calc_force(sun, planet1)
        planet1.force = calc_force(planet1, sun)
        print(planet1.force)
        sun.p = sun.p + sun.force * dt
        planet1.p = planet1.p + planet1.force*dt
        sun.pos = sun.pos + sun.p / sun.mass*dt
        planet1.pos = planet1.pos + planet1.p / planet1.mass*dt
    if Dec_Rate:
        rate(10)
        sun.force = calc_force(sun, planet1)
        planet1.force = calc_force(planet1, sun)
        print(planet1.force)
        sun.p = sun.p + sun.force * dt
        planet1.p = planet1.p + planet1.force*dt
        sun.pos = sun.pos + sun.p / sun.mass*dt
        planet1.pos = planet1.pos + planet1.p / planet1.mass*dt



#scene.range = 20
#if True:
    k = keysdown() # a list of keys that are down
    if 'down' in k: rate = 10000
    if 'up' in k: rate = 10
