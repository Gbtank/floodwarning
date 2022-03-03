from .station import MonitoringStation
from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """Takes a list of stations with an already updated
    water level, and returns a list of tuples (station object, water level)
    which have a water level greater than `tol`
    sorted by water level.
    """
    result = []
    for station in stations:
        level = station.relative_water_level()
        if level is not None and level > tol:
            result.append((station, level))

    return sorted_by_key(result, 1, reverse=True)

def stations_highest_rel_level(stations, N):
    """Takes a lsit of stations with an already updated
    water level, and returns of a list of N tuples, (station object, water level),
    which have the relative water levels and are sorted in descending water level
    order.
    """
    result = []
    for station in stations:
        level = station.relative_water_level()
        if level is not None:
            result.append((station, level))
    return sorted_by_key(result, 1, reverse=True)[:N]
