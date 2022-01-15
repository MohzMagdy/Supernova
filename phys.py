from vpython import vector, mag, sphere
from rate import get_dt

planets_list = []

def make_planets(uncreated_planets): # headers = ['ID', 'Mass', 'Velocity', 'Temperature', 'Position']
    global planets_list
    if len(uncreated_planets) > 0:
        used_ids = [planet.id for planet in planets_list]

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
                        radius = 0.2, p = vector(0,0,0), 
                    )
                    planet.p = planet.mass * planet.vel

                    planets_list.append(planet)
                except:
                    print('Invalid data!')


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
