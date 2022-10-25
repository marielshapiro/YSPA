import numpy as np
import matplotlib.pyplot as plt
import math

def LSRL(xlist,ylist):
    N = xlist.size
    inv = np.array([[N, np.sum(xlist)], [np.sum(xlist),np.sum(xlist**2)]])
    inv = np.linalg.inv(inv)

    mat = np.array([np.sum(ylist), np.sum(xlist*ylist)])

    solution = np.matmul(inv,mat)

    return solution

sg, sr, SG, SR = np.loadtxt('FullAlbedoData.csv', skiprows = 1, unpack = True, usecols = (4,5,6,7) , delimiter = ',')

# for index in range(sg.size):
#     if sg[index]-sr[index]>2:
#         print(index)
#         print(sg[index])
# sg = np.delete(sg,20)
# sr = np.delete(sr,20)
# SR=np.delete(SR,20)
# SG = np.delete(SG,20)

x = np.linspace(-.2,0.8)

y = LSRL(sg-sr,SG-SR)[1]*x + LSRL(sg-sr,SG-SR)[0]

plt.scatter(sg-sr, SG-SR)
plt.title("Instrumental vs Apparent Magnitude Calibration")
plt.ylabel("SG - SR (Apperent Mag)")
plt.xlabel("sg - sr (Instrumental Mag)")
plt.plot(x,y,color = 'r')
plt.show()



ASTsg = -9.006467573
ASTsr = -9.548233416

val = ASTsg-ASTsr

color_index = LSRL(sg-sr,SG-SR)[1]*val + LSRL(sg-sr,SG-SR)[0]
print("Color index = ", color_index)