# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key

def rivers_with_station(stations):
    """Takes a list of stations and
    returns all unique rivers associated
    with the stations.
    """
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    return rivers

def stations_by_river(stations):
    """Takes a list of MonitoringStation
    objects and maps each station's name (value) to its
    respective river (key).
    """
    station_map = {}
    for station in stations:
        if station.river in station_map:
            station_map[station.river].add(station.name)
        else:
            station_map[station.river] = { station.name }
    
    return station_map

def rivers_by_station_number(stations, N):
    """Determines N rivers with the greatest
    number of stations. If there are duplicate
    station numbers, the returned list can have
    more than N entries.
    """
    river_map = {}
    for station in stations:
        if station.river in river_map:
            river_map[station.river] = river_map[station.river] + 1
        else:
            river_map[station.river] = 1 

    river_list = [(river, number) for river, number in river_map.items()]
    river_list = sorted_by_key(river_list, 1, reverse=True)

    return_list = []
    # Use entries variable instead of O(n) #len()
    entries = 0

    station_number = 0
    for (river, number) in river_list:    
        if entries >= N:
            # Number of entries exceeds limit.
            if number != station_number:
                # Current number is not the same as last, so break.
                break

        # Entries less than limit, can append.        
        # Or entries exceeds N but the current number is the same as last.
        return_list.append((river, number))
        entries += 1
        station_number = number

    return return_list
