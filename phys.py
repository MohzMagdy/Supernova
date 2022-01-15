from vpython import vector, mag, sphere, gcurve, arange, color, graph, hat
from rate import get_dt
import math
import numpy as np

# List with all planet objects
planets_list = []

# Takes list of data of imported planets and creates planet object
def make_planets(uncreated_planets): 
    global planets_list
    if len(uncreated_planets) > 0: # Checks that planets were imported without errors
        used_ids = [planet.id for planet in planets_list] # Checks that IDs are unique

        for planet_data in uncreated_planets:
            if planet_data['id'] in used_ids:
                print('A planet with ID: \'%s\' already exists!' %planet_data['id'])
                continue
            else:
                try:
                    planet = sphere(
                        id = planet_data['id'], 
                        mass = planet_data['mass'], 
                        vel = vector(planet_data['vel'][0], planet_data['vel'][1], planet_data['vel'][2]),
                        temp = planet_data['temp'],
                        pos = vector(planet_data['pos'][0], planet_data['pos'][1], planet_data['pos'][2]),
                        radius = 0.2, p = vector(0,0,0)
                    )
                    planet.p = planet.mass * planet.vel
                    planet.color=hat(calc_color(planet))

                    planets_list.append(planet)
                except:
                    print('Invalid data!')

# Takes list of planets and outputs their data in a dictionary for exporting
def compile_planets(planets_list):
    planets_data = []

    for planet in planets_list:
        planet_data = {
        'id': planet.id,
        'mass': planet.mass,
        'vel': [planet.p.x/planet.mass, planet.p.y/planet.mass, planet.p.z/planet.mass],
        'temp': planet.temp,
        'pos': [planet.pos.x, planet.pos.y, planet.pos.z]
        }

        planets_data.append(planet_data)
    return planets_data

# Takes 2 planets and calculates force between them using Newton's second law
def calc_force(planet1, planet2):
    G = 1
    distance_vector = planet1.pos - planet2.pos
    rhat = distance_vector / mag(distance_vector)
    force = - G * planet1.mass * planet2.mass / (mag(distance_vector))**2 
    force_vector = force * rhat
    return force_vector

# Takes 2 planets and calculates their motion according to force and momentum
def move_planet(planet1, planet2):
    dt = get_dt()

    planet1.force = calc_force(planet1, planet2)
    planet2.force = calc_force(planet2, planet1)
    planet1.p = planet1.p + planet1.force * dt
    planet2.p = planet2.p + planet2.force * dt
    planet1.pos = planet1.pos + (planet1.p / planet1.mass) * dt
    planet2.pos = planet2.pos + (planet2.p / planet2.mass) * dt
    return ((planet1.pos, planet1.p), (planet2.pos, planet2.p))

# Takes a planet ID and draws its radiation graph
def calc_rad(id):
    global planets_list

    planet = 0
    for p in planets_list:
        if p.id == id:
            planet = p
            break
        
    if planet == 0:
        print('Invalid ID')
        return

    gd = graph(width=600, height=250,
        title='<b>Blackbody Radiation</b>',
        xtitle='<i>Lambda</i>', ytitle='<i>Radiation</i>',
        foreground=color.black, background=color.white)
    curve= gcurve(color=color.black)
    h=6.626*10**-34
    c=3*10**8
    k=1.38*(10**-23)
    try:
        for y in arange(200,3000,2)*10**-9:
            D=(2*h* (c**2) )/(y)**5
            F=(h*c)/(y*k*planet.temp)
            G=(2.718**(F))
            B=D/(G-1)
            
            curve.plot(y,B)
    except:    
        print('Planet temperature too low')


# Takes a planet object and calculates its color according to temperature
def calc_color(planet):
    r=[]
    g=[]
    b=[]
    h=6.626*10**-34
    c=3*10**8
    k=1.38*(10**-23)
    
    try:
        for y in range (650,700):
            D=(2*h* (c**2) )/(y*(10**-9))**5
            F=(h*c)/(y*(10**-9)*k*(planet.temp))
            G=(2.718**(F))
            B=D/(G-1)
            x=4*3.14*((planet.radius)**2)*B
            r.append(x)

        for y in range (550,580):
            D=(2*h* (c**2) )/(y*(10**-9))**5
            F=(h*c)/(y*(10**-9)*k*(planet.temp))
            G=(2.718**(F))
            B=D/(G-1)
            x=4*3.14*((planet.radius)**2)*B
            g.append(x)

        for y in range (450,500):
            D=(2*h* (c**2) )/(y*(10**-9))**5
            F=(h*c)/(y*(10**-9)*k*(planet.temp))
            G=(2.718**(F))
            B=D/(G-1)
            x=4*3.14*((planet.radius)**2)*B
            b.append(x)
    except:
        return vector(255,255,255)

    rr = np.trapz(r)
    gg = np.trapz(g)
    bb = np.trapz(b)

    color = vector(rr%255,gg%255,bb%255)
    return color

# Takes planet ID and calculates its luminosity
def calc_luminosity(id):
    global planets_list

    planet = 0
    for p in planets_list:
        if p.id == id:
            planet = p
            break
        
    if planet == 0:
        print('Invalid ID')
        return

    surface_area = 4*math.pi*(planet.radius)**2
    lum = surface_area *(5.67*10**-8)* (planet.temp**4)
    print('Luminosity = ', lum)

# Calculates the center of mass for a planet
def calc_COM(id1, id2):
    global planets_list

    com = 0
    for i in range(len(planets_list)):
        if id1 == planets_list[i].id:
            for j in range(len(planets_list)):
                if id2 == planets_list[j].id:
                    com = ((planets_list[i].mass*planets_list[i].pos) + (planets_list[j].mass*planets_list[j].pos))/\
                            (planets_list[i].mass+planets_list[j].mass)

    print('Center of Mass = ', com)