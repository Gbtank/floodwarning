from floodsystem import geo
from floodsystem.stationdata import build_station_list

def run():
    """Prints the number of rivers with a station and
    prints the first 10 stations at the rivers
    River Aire, River Cam, and River Thames
    in alphabetical order.
    """
    # Build station list
    stations = build_station_list()
    # List of rivers with atleast one monitoring station
    rivers = geo.rivers_with_station(stations)
    # Number of rivers with atleast one monitoring station 
    num = len(rivers)
    first_ten = sorted(rivers)[:10] 
    print(f'{num} stations. First 10 - {first_ten}')

    river_map = geo.stations_by_river(stations)
    print(sorted([station.name for station in river_map["River Aire"]]))
    print(sorted([station.name for station in river_map["River Cam"]]))
    print(sorted([station.name for station in river_map["River Thames"]]))

if __name__ == "__main__":
    print("*** Task1D: CUED Part IA ***")
    run()
