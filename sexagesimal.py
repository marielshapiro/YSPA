def toSexagesimal(angle):
    degrees = int(abs(angle))
    arcmin = int((abs(angle) - int(abs(angle)))*60.0)
    arcsec = (((abs(angle) - int(abs(angle)))*60.0) - arcmin)*60.0
    if angle<0:
        degrees = -1*degrees
    return (degrees, arcmin, arcsec )
def toDecimal(degrees, arcmin, arcsec):
    sum = abs(degrees) + arcmin/60+arcsec/3600
    if degrees<0:
        sum*=-1
    return sum


