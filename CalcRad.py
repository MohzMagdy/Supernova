from vpython import *

# def CalcRad(T):
gd = graph(width=600, height=250,
    title='<b>Blackbody Radiation</b>',
    xtitle='<i>Lamda</i>', ytitle='<i>Radiation</i>',
    foreground=color.black, background=color.white)
curve= gcurve(color=color.black)
h=6.626*10**-34
c=3*10**8
k=1.38*(10**-23)
T=5777
for y in arange(2,40,2)*10**-9:
    # B=y**2
    D=(2*h* (c**2) )/(y)**5
    F=(h*c)/(y*k*T)
    G=(2.718**(F))
    B=D/(G-1)
    
    curve.plot(y,B)

# def max_lamda(T):
#     y_max=T*0.002897755
#     print('maximum lamda',y_max)



# T=7000
# CalcRad(T)