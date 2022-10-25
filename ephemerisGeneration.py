import jplephem
from jplephem.spk import SPK
import numpy as np
from vpython import *
import math

Km = 1.496e8
kernel = SPK.open('de421.bsp')
#print(kernel)



position = kernel[0,3].compute(2459786.7083333335)
#print(position)

R = -vector(position[0],position[1],position[2])*6.68459e-9

r = vector(0.544448, -0.790835, -0.34144)

r = r.rotate(angle = radians(23.4), axis = vector(1,0,0))




rho = r+R
rhohat = rho/rho.mag



dec = math.asin(rhohat.z)
ra = math.acos(abs(rhohat.x)/math.cos(dec))


if rhohat.x<0 and rhohat.y<0:
        ra = 2*pi - ra
elif rhohat.x>0 and rhohat.y<0:
        ra = 2*pi-ra

        
ra = degrees(ra)/15

def toSexagesimal(angle):
    degrees = int(angle)
    arcmin = int((angle - int(angle))*60.0)
    arcsec = (((angle - int(angle))*60.0) - arcmin)*60.0
    return (degrees, arcmin, arcsec )


ra = toSexagesimal(ra)
dec = toSexagesimal(degrees(dec))
print(f"Geocentric Dec: {dec}")
print(f"Geocentric RA: {ra}")

