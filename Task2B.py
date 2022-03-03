from floodsystem import flood
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    # Build station list
    stations = build_station_list()

    # Update water levels
    update_water_levels(stations)

    # Filter station list for stations that have a relative
    # water level over 0.8
    result = flood.stations_level_over_threshold(stations, 0.8)
    for (station, level) in result:
        print(f"{station.name} {level}")

if __name__ == "__main__":
    run()
