from floodsystem.stationdata import build_station_list
from floodsystem import station

def run():
    stations = build_station_list()
    
    inconsistent_stations = station.inconsistent_typical_range_stations(stations)
    names = [station.name for station in inconsistent_stations]
    names.sort()
    print(names)

if __name__ == "__main__":  
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
