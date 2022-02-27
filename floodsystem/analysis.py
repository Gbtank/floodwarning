import numpy as np
import matplotlib

def polyfit(dates, levels, p):
    d = matplotlib.dates.date2num(dates)
    poly = np.poly1d(d - d[0], levels, p)
    return (poly, d[0])
