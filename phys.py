from vpython import vector, mag, sphere
from rate import get_dt

def calc_force(planet1, planet2):
    G = 1
    distance_vector = planet1.pos - planet2.pos
    rhat = distance_vector / mag(distance_vector)
    force = - G * planet1.mass * planet2.mass / (mag(distance_vector))**2 
    force_vector = force * rhat
    return force_vector

def move_planet(planet1, planet2):
    dt = get_dt()

    planet1.force = calc_force(planet1, planet2)
    planet2.force = calc_force(planet2, planet1)
    planet1.p = planet1.p + planet1.force * dt
    planet2.p = planet2.p + planet2.force * dt
    planet1.pos = planet1.pos + (planet1.p / planet1.mass) * dt
    planet2.pos = planet2.pos + (planet2.p / planet2.mass) * dt
    return ((planet1.pos, planet1.p), (planet2.pos, planet2.p))

planets_list = []
planets_data = []
def make_planets(uncreated_planets): # headers = ['ID', 'Mass', 'Velocity', 'Temperature', 'Position'] #Add: Radius, optional texture
    global planets_list, planets_data

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

