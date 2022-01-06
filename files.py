import csv

#Planet attributes: id, mass, initial velocity vector "x,y,z" , temperature, initial position vector "x,y,z"
def from_file(path):
    fh = open(path, 'r') #'.\\Presets\\'+
    reader = csv.reader(fh)

    planets = []
    
    isHeader = True
    for row in reader:
        if isHeader: #Skips headers in csv
            isHeader = False
            continue
        if len(row) == 0: #Skips empty lines in csv
            continue
        
        planet = {
            'id': row[0], 
            'mass': float(row[1]),
            'vel': [float(v) for v in row[2].split(',')],
            'temp': float(row[3]),
            'pos': [float(v) for v in row[4].split(',')]
        }
        planets.append(planet)
    
    fh.close()
    return planets

def to_file(path, planets):
    fh = open(path, 'w')
    writer = csv.writer(fh)

    headers = ['ID', 'Mass', 'Velocity', 'Temperature', 'Position']
    writer.writerow(headers)

    for planet in planets:
        values = [
            planet['id'],
            planet['mass'],
            ','.join([str('%.2f' %v) for v in planet['vel']]),
            planet['temp'],
            ','.join([str('%.2f' %v) for v in planet['pos']])
        ]
        writer.writerow(values)
    
    fh.close()