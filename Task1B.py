git clone <https://github.com/Gbtank/floodwarning.git>

pip install requests
pip install python-dateutil

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    #Task 1B subtasks

    # Build list of stations
    stations = build_station_list()
    # Find distances of all stations from Cambridge
    distance_list = stations_by_distance(stations, (52.2053, 0.1218))

    namelist = [(station.name, station.town, distance)
                for (station, distance) in distance_list]

    print(namelist[:10])
    print("\n")
    print(namelist[-10:])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System *** \n")

    # Run Task1B
    run()
    
