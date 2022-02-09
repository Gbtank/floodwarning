from floodsystem import geo
from floodsystem.stationdata import build_station_list


def run():
    """Prints a list of tuples (station name, town, distance) 
    for the 10 closest and the 10 furthest stations 
    from the Cambridge city centre, (52.2053, 0.1218).
    """

    # Build list of stations
    stations = build_station_list()
    # Find distances of all stations from Cambridge
    station_distances = geo.stations_by_distance(stations, (52.2053, 0.1218))
    # Using list comprehension create a list of 3-tuples out of the previous list
    output_list = [(station.name, station.town, distance) for (station, distance) in station_distances]

    print("Closest 10 stations")
    print(output_list[:10])
    print("Furthest 10 stations")
    print(output_list[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
