from floodsystem.stationdata import build_station_list
from floodsystem import station

def run():
    # Build station list
    stations = build_station_list()
    
    # Creates a list of inconsistent station objects
    inconsistent_stations = station.inconsistent_typical_range_stations(stations)
    # Using list comprehension, creates a list of station names from station objects
    # and then sorts into alphabetical order
    names = sorted([station.name for station in inconsistent_stations])
    print(names)

if __name__ == "__main__":  
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
