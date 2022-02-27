from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem import flood

def run():
    stations = build_station_list()

    update_water_levels(stations)

    result = flood.stations_highest_rel_level(stations, 10)
    for (station, level) in result:
        print(f"{station.name} {level}")

if __name__ == "__main__":
    run()
