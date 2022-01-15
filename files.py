import csv

#Planet attributes: id, mass, initial velocity vector "x,y,z" , temperature, initial position vector "x,y,z"

# Takes a file name and imports planets from its rows
def from_file(path):
    try:
        fh = open('Presets\\' + path, 'r') 
    except:
        print('Incorrect file Name!')
        return []

    reader = csv.reader(fh)
    
    planets_data = []
    
    isHeader = True
    for row in reader:
        if isHeader: #Skips headers in csv
            isHeader = False
            continue
        if len(row) == 0: #Skips empty lines in csv
            continue
        try:
            planet = {
                'id': row[0], 
                'mass': float(row[1]),
                'vel': [float(v) for v in row[2].split(',')],
                'temp': float(row[3]),
                'pos': [float(v) for v in row[4].split(',')]
            }

            planets_data.append(planet) 
        except:
            print('Invalid data!')
    
    fh.close()
    return planets_data


# Takes a list of dictionaries of planets data and exports them into a file of the given name
def to_file(path, planets_data):
    fh = open('Presets\\' + path, 'w')
    writer = csv.writer(fh)

    headers = ['ID', 'Mass', 'Velocity', 'Temperature', 'Position']
    writer.writerow(headers)

    for planet in planets_data:
        values = [
            planet['id'],
            planet['mass'],
            ','.join([str('%.2f' %v) for v in planet['vel']]),
            planet['temp'],
            ','.join([str('%.2f' %v) for v in planet['pos']])
        ]
        writer.writerow(values)
    
    fh.close()