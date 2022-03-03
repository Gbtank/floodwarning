from floodsystem import flood
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()

    update_water_levels(stations)

    result = flood.stations_level_over_threshold(stations, 0.8)
    for (station, level) in result:
        print(f"{station.name} {level}")

if __name__ == "__main__":
    run()
