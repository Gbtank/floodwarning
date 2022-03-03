from .station import MonitoringStation
from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    result = []
    for station in stations:
        level = station.relative_water_level()
        if level is not None and level > tol:
            result.append((station, level))

    return sorted_by_key(result, 1, reverse=True)

def stations_highest_rel_level(stations, N):
    result = []
    for station in stations:
        level = station.relative_water_level()
        if level is not None:
            result.append((station, level))
    return sorted_by_key(result, 1, reverse=True)[:N]
