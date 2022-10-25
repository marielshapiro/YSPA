import numpy as np
import matplotlib.pyplot as plt

ra, dec, sg, sr = np.loadtxt('fixedapassAlbedoData.csv', skiprows = 1, unpack = True, delimiter = ',')

ra/=15


RA, DEC = np.loadtxt('Albedo Calculation - Sheet1.csv', skiprows = 1, usecols = (0,1), unpack = True, delimiter = ',')
plt.scatter(ra,dec, s=(10*(sg.max()-sg)), facecolor='none', edgecolor='g')



    
tuplist = []
xlist = []
for index in range(RA.size):
    tuplist.append((round(RA[index],2),round(DEC[index],2)))
    xlist.append(round(RA[index],2))
    mindiff = 5
    for place in range(ra.size):
        
        newdiff = abs(RA[index] - ra[place])
        
        if newdiff<mindiff:
            mindiff = newdiff
            store = place
            
    print(f"RA APASS = {ra[store]}, RA = {RA[index]}, SG = {sg[store]}, SR - {sr[store]}")    

# for i, label in enumerate(xlist):
#     plt.annotate(str(label), (RA[i], DEC[i]), fontsize='xx-small')
    
plt.scatter(RA, DEC, s = 5, color = 'r')
plt.xlim(15.04,15.10)
plt.legend(['APASS Absolute Magnitudes', 'Reference Stars'], loc ="upper right", prop={'size': 6})
plt.title('APASS Sloan Green Magnitudes')
plt.xlabel('RA (hr)')
plt.ylabel('Dec (degrees)')
plt.show()