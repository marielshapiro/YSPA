import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#JD, MAG = np.loadtxt("lightcurve_jul14.csv", skiprows = 1, usecols = (1,7), unpack = True, delimiter = ",")
JD, MAG = np.loadtxt("Lightcurve_Jul30_updated.csv", skiprows = 1, usecols = (1,7), unpack = True, delimiter = ",")

TIME = JD - JD[0]

index = [i for i in range(10,29)]
TIME = np.delete(TIME, index)
MAG = np.delete(MAG, index)

def sine(x,A,T,phase,offset):
    return A*np.sin(x/T*2*np.pi+phase)+offset

# index = [0,1,2,3,4,5,6]
# index = [0]
# JD = np.delete(JD, index)
# MAG = np.delete(MAG, index)

# index = [6,7]
# JD = np.delete(JD, index)
# MAG = np.delete(MAG, index)

# index = [6,8,9,11]
# TIME = np.delete(TIME, index)
# MAG = np.delete(MAG, index)

popt,pcov=curve_fit(sine,TIME,MAG,p0=(2,1/24,0,15))
print(popt)
plt.xlabel("Time (days)")
plt.ylabel("Magnitude")
plt.title("Magnitude vs. Time")

x = np.linspace(-0.1,0.1)
plt.scatter(TIME, MAG)
plt.plot(x,sine(x,*popt))
plt.show()

# JD2, MAG2 = np.loadtxt("lightcurve_2.csv", skiprows = 1, usecols = (1,7), unpack = True, delimiter = ",")
# plt.scatter(JD2, MAG2)
# plt.show()