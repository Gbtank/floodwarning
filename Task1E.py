from floodsystem.stationdata import build_station_list
from floodsystem import geo

def run():
    """Prints a list of tuples (river, number stations)
    which is at least N = 9 entries in length.
    """

    # Build station list
    stations = build_station_list()

    # Create a tuple of (river, number stations) for N = 9
    rivers = geo.rivers_by_station_number(stations, 9)
    print(rivers)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***") 
    run()
