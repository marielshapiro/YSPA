import matplotlib.pyplot as plt
import math
import numpy as np

t = 0
dt= .1
radius = 1
g = 9.8
theta = math.pi/40
vel = 0
pos = theta + 1/2*-1*(g/radius)*math.sin(theta)*dt**2


tlist = [0,dt]
poslist = [theta,pos]
actlist = []
errorlist = []
index = 2

while t<20: 
    actual = theta*math.cos(math.sqrt(g/radius)*(t))
    
    acceleration = -1*(g/radius)*math.sin(poslist[index-1])
    
    pos = 2*poslist[index-1] - poslist[index-2] + acceleration*dt**2
    poslist.append(pos)
    
    tlist.append(t)
    errorlist.append(actual-pos)
    actlist.append(actual)
    
    index+=1
    t+=dt

altt = tlist[2:]

plt.plot(tlist,poslist)
plt.plot(altt,actlist)
plt.plot(altt,errorlist)
plt.show()
    