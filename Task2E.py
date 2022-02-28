from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels

import datetime

def run():
    stations = build_station_list()
    risky_stations = stations_highest_rel_level(stations, 5)
    delta = datetime.timedelta(days=10)
    
    for station in risky_stations:
        dates, levels = fetch_measure_levels(station.measure_id, delta)
        plot_water_levels(station, dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()