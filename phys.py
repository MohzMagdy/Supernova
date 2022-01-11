from vpython import *

def calc_force(planet1, planet2):
    G = 1
    distance_vector = planet1.pos - planet2.pos
    rhat = distance_vector / mag(distance_vector)
    force = - G * planet1.mass * planet2.mass / (mag(distance_vector))**2 
    force_vector = force * rhat
    return force_vector

dt = 0.01
def move_planet(planet1, planet2):
    global dt

    planet1.force = calc_force(planet1, planet2)
    planet2.force = calc_force(planet2, planet1)
    # print(planet1.force)
    planet1.p = planet1.p + planet1.force * dt
    planet2.p = planet2.p + planet2.force * dt
    planet1.pos = planet1.pos + (planet1.p / planet1.mass) * dt
    planet2.pos = planet2.pos + (planet2.p / planet2.mass) * dt
    return ((planet1.pos, planet1.p), (planet2.pos, planet2.p))

