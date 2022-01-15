from vpython import *
def luminosity(object):
    l=4*3.14* ((object.radius)**2) *(5.67*10**-8)* (object.temp**4)
    ll=l%10
    scene.lights=[]
    object=local_light(pos=object.pos, color=color.gray(ll))
    print(ll)

p1=sphere(pos=vector(2,2,2),radius=1,color=color.white)
p2=sphere(pos=vector(-5,2,2),radius=1,color=color.white)
p3=sphere(pos=vector(7,-2,2),radius=1,color=color.blue)
p4=sphere(pos=vector(-2,-9,2),radius=1,color=color.white)
s=sphere(pos=vector(0,0,0),radius=0.5,temp=7000,color=color.yellow,emissive=True)
luminosity(s)