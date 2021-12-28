from vpython import *
from rate import *
from files import *
from console import *   

global planets_list 
planets_list = []

# Import and Export buttons
def console_import():
    global planets_list
    planets_list.append(from_console())
button(bind = console_import, text = 'Console Import')

def console_export():
    global planets_list
    to_console(planets_list)
button(bind = console_export, text = 'Console Export')

def file_import():
    global planets_list
    planets_list.extend(from_file(input('Enter file Path: ')))
button(bind = file_import, text = 'File Import')

def file_export():
    global planets_list
    to_file(input('Enter file Path: '),planets_list)
button(bind = file_export, text = 'File Export')


# Test Sphere
test_s = sphere(pos=vector(2,2,0), make_trail = True, trail_type = 'points', interval = 5, retain = 15) # Test sphere
test_s.p = vector(0,0,5) # Sphere angular momentum

def Pause():
    global rate_value
    rate_value = 1
    return
button(bind = Pause, text = 'Pause')

# Main run loop
dt = 0.01
while True:
    rate(rate_value)
    F = - 50 * test_s.pos.hat / mag2(test_s.pos)
    test_s.p += F*dt
    test_s.pos = test_s.pos + test_s.p*dt
