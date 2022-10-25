from vpython import *

scene.camera.rotate(axis = vector(0,1,0), angle = -pi/2) #makes the clock face the camera

face = cylinder(axis = vector(0.1,0,0)) #makes the face of the clock, a thin cylinder

hhand=arrow(axis = vector(0,.8,0), color = color.black) #sets the hour minute and second hands, has them point up in the y direction
mhand=arrow(axis = vector(0,.8,0), color = color.blue)
shand=arrow(axis = vector(0,.8,0), color = color.red)

dt = 0.01
t = 0

for n in range(1,13): #iteragtes through the hours
    angle = n/12 * 2*pi #calculates the angle in radians
    label(pos =(vector(0,cos(angle),sin(angle))), text = str(n)) #puts a number label at each hour around the face
    box(pos = vector(0,cos(angle)/1.2,sin(angle)/1.2), axis = vector(sin(angle),1,0),color = color.black,length = .05, height = .05, width = .05)#puts the tick marks on the circle

while t<1000:
    #uses the axis attributes to rotate the axes of the arrows each second
    shand.axis = rotate(shand.axis,radians(6), axis = vector(1,0,0))
    mhand.axis = rotate(mhand.axis,radians(1/10), axis = vector(1,0,0))
    hhand.axis = rotate(hhand.axis,radians(1/240), axis = vector(1,0,0))
    t+=dt
    rate(1)
 
