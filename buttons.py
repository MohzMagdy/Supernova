from vpython import button, sphere
from console import *
from files import *
from rate import *
from phys import *

#Import and Export buttons
def console_import():
    global running
    if running:
        pause()
    new_planets = []
    new_planets.append(from_console())
    make_planets(new_planets)
    if not running:
        pause()
button(bind = console_import, text = 'Console Import')

def console_export():
    global planets_data
    to_console(planets_data)
button(bind = console_export, text = 'Console Export')

def file_import():
    global running
    if running:
        pause()
    new_planets = []
    new_planets.extend(from_file(input('Enter file Name: ')))
    make_planets(new_planets)
    if not running:
        pause()
button(bind = file_import, text = 'File Import')

def file_export():
    global planets_data
    to_file(input('Enter file Name: '), planets_data)
button(bind = file_export, text = 'File Export')


# Rate buttons
button(bind = inc_rate, text = 'Increase Rate')
button(bind = dec_rate, text = 'Decrease Rate')

# Planet buttons
def clear_planets():
    global planets_list, default_planets_button, running
    if running:
        pause()
    for i in range(len(planets_list)):
        planets_list[i].visible = False
    planets_list.clear()
    default_planets_button = button(bind = default_planets, text = 'Add Sun & Earth')
button(bind = clear_planets, text = 'Clear Planets')

# Earth and Sun button
def default_planets():
    global planets_list, default_planets_button
    sun = sphere(id = 1, pos=vector(0,0,0), radius = 0.8, mass = 1500 , p = vector(0,0,0),  texture= 'Assets\\Sun.jpg')
    earth = sphere(id = 2, pos = vector(2,0,0), radius = 0.2, mass=1, p = vector(0,30,0), texture = 'Assets\\Earth.jpg')

    planets_list.append(sun)
    planets_list.append(earth)
    default_planets_button.delete()
default_planets_button = button(bind = default_planets, text = 'Add Sun & Earth')