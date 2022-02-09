from floodsystem import geo
from floodsystem.stationdata import build_station_list

def run():
    """Uses the function geo.stations_within_radius to 
    build a list of stations within 10 km of the Cambridge city centre (coordinate (52.2053, 0.1218)). 
    Print the names of the stations, listed in alphabetical order.
    """

    # Build station list
    stations = build_station_list()

    # Create new list of stations consisting of only the stations which fit in the 10km radius of (52.2053, 0.1218)
    central_stations = geo.stations_within_radius(stations, (52.2053, 0.1218), 10)
    # Using list comprehension generate a list of station names and then sort.
    station_names = sorted([station.name for station in central_stations])
    print(station_names)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
