import numpy as np
import matplotlib

def polyfit(dates, levels, p):
    d = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(d - d[0], levels, p)
    poly = np.poly1d(p_coeff)
    return (poly, d[0])