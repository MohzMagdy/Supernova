from vpython import button, sphere
from console import *
from files import *
from rate import *
from phys import *

#Import and Export buttons
def console_import():
    global get_running
    if get_running():
        pause()
    make_planets(from_console())
    if not get_running():
        pause()
button(bind = console_import, text = 'Console Import')

def console_export():
    global planets_list
    to_console(compile_planets(planets_list))
button(bind = console_export, text = 'Console Export')

def file_import():
    global get_running
    if get_running():
        pause()
    new_planets = []
    new_planets.extend(from_file(input('Enter file Name: ')))
    make_planets(new_planets)
    if not get_running():
        pause()
button(bind = file_import, text = 'File Import')

def file_export():
    global planets_list
    to_file(input('Enter file Name: '), compile_planets(planets_list))
button(bind = file_export, text = 'File Export')


# Rate buttons
button(bind = inc_rate, text = 'Increase Rate')
button(bind = dec_rate, text = 'Decrease Rate')

# Planet buttons
def clear_planets():
    global planets_list, default_planets_button, get_running, default_planets_button_exist
    if get_running():
        pause()
    for i in range(len(planets_list)):
        planets_list[i].visible = False
    planets_list.clear()
    if not default_planets_button_exist:
       default_planets_button = button(bind = default_planets, text = 'Add Sun & Earth')   
       default_planets_button_exist = True
button(bind = clear_planets, text = 'Clear Planets')

# Earth and Sun button
def default_planets():
    global planets_list, default_planets_button, default_planets_button_exist
    sun = sphere(id = 'sun', pos=vector(0,0,0), radius = 0.8, mass = 1500 , p = vector(0,0,0), temp = 5000, texture= 'Assets\\Sun.jpg')
    earth = sphere(id = 'earth', pos = vector(2,0,0), radius = 0.2, mass=1, p = vector(0,30,0), temp = 40, texture = 'Assets\\Earth.jpg')

    planets_list.append(sun)
    planets_list.append(earth)

    default_planets_button.delete()
    default_planets_button_exist = False
default_planets_button = button(bind = default_planets, text = 'Add Sun & Earth')
default_planets_button_exist = True