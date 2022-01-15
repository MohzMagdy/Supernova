def from_console():
    try:
        planet = {
            'id': input('Enter ID: '), 
            'mass': float(input('Enter Mass: ')),
            'vel': [float(v) for v in input('Enter Velocity: ').split(',')],
            'temp': float(input('Enter Temperature: ')),
            'pos': [float(v) for v in input('Enter Position: ').split(',')]
        }

        return [planet]
    except:
        print('Invalid data!')
    return []

def to_console(planets_data):
    for planet in planets_data:
        print('ID: %s, Mass: %.2f, Velocity: (%s), Temperature %.2f, Position: (%s)' 
        %(planet['id'], 
        planet['mass'], 
        ','.join([str('%.2f' %v) for v in planet['vel']]), 
        planet['temp'], 
        ','.join([str('%.2f' %v) for v in planet['pos']]))
        )