from vpython import *
import numpy as np

# import math
# import numpy as N
# import scipy as s

# from scipy.integrate import quad


def CalcRad(object):
    gd = graph(width=600, height=250,
        title='<b>Blackbody Radiation</b>',
        xtitle='<i>Lamda</i>', ytitle='<i>Radiation</i>',
        foreground=color.black, background=color.white)
    curve= gcurve(color=color.black)
    h=6.626*10**-34
    c=3*10**8
    k=1.38*(10**-23)
    for y in arange(200,3000,2)*10**-9:
        D=(2*h* (c**2) )/(y)**5
        F=(h*c)/(y*k*object.temp)
        G=(2.718**(F))
        B=D/(G-1)
        
        curve.plot(y,B)

def max_lamda(object):
    y_max=object.temp*0.002897755
    print('maximum lamda',y_max)


def colorrr(object):
    r=[]
    g=[]
    b=[]
    h=6.626*10**-34
    c=3*10**8
    k=1.38*(10**-23)

    for y in range (650,700):
        D=(2*h* (c**2) )/(y*(10**-9))**5
        F=(h*c)/(y*(10**-9)*k*(object.temp))
        G=(2.718**(F))
        B=D/(G-1)
        x=4*3.14*((object.radius)**2)*B
        r.append(x)

    for y in range (550,580):
        D=(2*h* (c**2) )/(y*(10**-9))**5
        F=(h*c)/(y*(10**-9)*k*(object.temp))
        G=(2.718**(F))
        B=D/(G-1)
        x=4*3.14*((object.radius)**2)*B
        g.append(x)

    for y in range (450,500):
        D=(2*h* (c**2) )/(y*(10**-9))**5
        F=(h*c)/(y*(10**-9)*k*(object.temp))
        G=(2.718**(F))
        B=D/(G-1)
        x=4*3.14*((object.radius)**2)*B
        b.append(x)

    rr =np.trapz(r)
    gg =np.trapz(g)
    bb =np.trapz(b)

    # print(rr%255,gg%255,bb%255)
    collor =vector(rr%255,gg%255,bb%255)
    return collor



s=sphere(pos=vector(0,0,0),radius=89,temp=889630)
s.color=hat(colorrr(s))




# T=7000
# CalcRad(T)