from floodsystem import geo
from floodsystem.stationdata import build_station_list

def sort_and_limit(iterable, limit):
    """Utility function which sorts
    a list or set and returns the first
    `limit` entries in a list. 
    """
    return sorted(iterable)[:limit]

def run():
    """Task1D:
    Prints the number of rivers with a station and
    prints the first 10 stations at the rivers
    River Aire, River Cam, and River Thames
    in alphabetical order.
    """
    stations = build_station_list()
    rivers = geo.rivers_with_station(stations)
    num = len(rivers)
    first_ten = sort_and_limit(rivers, 10)
    print(f'{num} stations. First 10 - {first_ten}')

    river_map = geo.stations_by_river(stations)
    print(sort_and_limit(river_map["River Aire"], 10))
    print(sort_and_limit(river_map["River Cam"], 10))
    print(sort_and_limit(river_map["River Thames"], 10))

if __name__ == "__main__":
    print("*** Task1D ***")
    run()
