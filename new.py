from vpython import *
rate1 = 100
def Dec_Rate(rate1):
    while rate1 == 1000:
        rate1 = 10
        print(rate1)
scene.bind('click', Dec_Rate)
button( bind=Dec_Rate, text='Decrease Rate!')



def forcee(planet1, planet2):
    G = 1
    Distance_vector = planet1.pos - planet2.pos
    rhat = Distance_vector / mag(Distance_vector)
    force = -G * planet1.mass * planet2.mass / (mag(Distance_vector))**2
    force_vector = force * rhat
    return force_vector



sun = sphere(pos=vector(0,0,0), radius = 0.8
             ,texture="https://media.istockphoto.com/photos/realistic-sun-or-star-closeup-3d-rendering-illustration-picture-id1267178422?b=1&k=20&m=1267178422&s=170667a&w=0&h=EtPtCIh3MP5f2f9XjNxTHChncLA5WUeuY5TWVuP1SEs=",
             mass = 1500 , p = vector(0,0,0), make_Trail = True)
#sun.p = vector(0,0,5) # Sphere angular momentum
planet1 = sphere(pos= vector(2,0,0), radius = 0.2, mass=1, p = vector(0,30,0), make_Trail = True
                 ,texture = "https://upload.wikimedia.org/wikipedia/commons/6/60/Earth_from_Space.jpg")
#planet1.mass = 100
#planet1.p = vector(0, 0, 5)

dt = 0.0001
t = 0
while True:
    rate(rate1)
    sun.force = forcee(sun, planet1)
    planet1.force = forcee(planet1, sun)
    print(planet1.force)
    sun.p = sun.p + sun.force * dt
    planet1.p = planet1.p + planet1.force*dt
    sun.pos = sun.pos + sun.p / sun.mass*dt
    planet1.pos = planet1.pos + planet1.p / planet1.mass*dt


#scene.range = 20
#if True:
 #   k = keysdown() # a list of keys that are down
  #  if 'down' in k: rate1 = 10000
   # if 'up' in k: rate1 = 10