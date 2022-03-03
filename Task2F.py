from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
import numpy as np
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import *
import datetime

"""Task 2F: function fitting"""

def run():
    # Build list of stations
    stations  = build_station_list()
    risky_stations = stations_highest_rel_level(stations, 5)
    delta = datetime.timedelta(days=2)
    p=4 
    for station in risky_stations:
        dates, levels = fetch_measure_levels(station.measure_id, delta)
        poly, d0 = polyfit(dates, levels, p)
        plot_water_level_with_fit(station, dates, levels, p)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()