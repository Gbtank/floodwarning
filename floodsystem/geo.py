# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

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
