import vpython
from vpython import *
import matplotlib.pyplot as plt
import math

t = 0
dt = 9640
G = 6.67e-11
moondistance = 3.85e8
earthm = 5.97e24
eartha = vector(0, 0,0)

moona = vector(-G*earthm/moondistance**2,0,0)

earthv0 = vector(0,0,0)
earthx0 = vector(0,0,0)


moonx0 = vector(moondistance,0,0)
moonv0 = vector(0,math.sqrt(G*earthm/moondistance),0)
moonx1 = moonx0 + moonv0*dt +1/2 * moona * dt**2 
moonlastx = moonx1 
moonx_2 = moonx0

earth = sphere(pos = earthx0,color = color.blue,radius = 6.4e7, make_trail = True)
moon = sphere(pos = moonx1, color = color.white, radius = 1.7e6, make_trail = True)

while t<86400*30:
    
    
    XImoon = 2*moonlastx - moonx_2 + moona*dt**2
    moonvec = XImoon/XImoon.mag 
    moon.pos = XImoon
    moonx_2 = moonlastx
    moonlastx = XImoon
    moona = -1*moonvec*moona.mag 
    t+=dt
    rate(20)