def from_console():
    planet = {
        'id': input('Enter ID: '), 
        'mass': float(input('Enter Mass: ')),
        'vel': [float(v) for v in input('Enter Velocity: ').split(',')],
        'temp': float(input('Enter Temperature: ')),
        'pos': [float(v) for v in input('Enter Position: ').split(',')]
    }
    return planet

def to_console(planets):
    for planet in planets:
        print('ID: %s, Mass: %.2f, Velocity: (%s), Temperature %.2f, Position: (%s)' 
        %(planet['id'], 
        planet['mass'], 
        ','.join([str('%.2f' %v) for v in planet['vel']]), 
        planet['temp'], 
        ','.join([str('%.2f' %v) for v in planet['pos']]))
        )