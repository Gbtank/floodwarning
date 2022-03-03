from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem import flood

def run():
    # Build station list
    stations = build_station_list()

    # Update water levels
    update_water_levels(stations)

    # Get first 10 stations with the highest relative water level
    result = flood.stations_highest_rel_level(stations, 10)
    for (station, level) in result:
        print(f"{station.name} {level}")

if __name__ == "__main__":
    run()