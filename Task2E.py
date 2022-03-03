import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key


def run():
    """Demonstration Program for Task 2E"""

    stations = build_station_list()  # Create list of all stations
    update_water_levels(stations)  # Update the water levels
    dt = 10  # Number of days to plot
    N = 5  # Number of stations to plot
    waterlevellist = []  # Initialise list of stations and waterlevels
    for station in stations:  # iterate through all stations
        # Ensure that there is a waterlevel and the range is consistent
        if (station.typical_range_consistent() is True) and (type(station.relative_water_level()) is float):
            waterlevellist.append((station, station.relative_water_level()))  # Add station and its relative
            # waterlevel to the list
        else:
            pass  # Move to next station
    # print(waterlevellist)  # Used to test
    sortedwaterlevellist = sorted_by_key(waterlevellist, 1)  # Create sorted list (sorted by relative waterlevel)
    top5 = sortedwaterlevellist[-(N + 1):-1]  # Take the top N stations
    # print(top5)  # Used to test

    # Initialise lists
    dateslist = []
    levelslist = []
    top5stations = []

    for j in range(len(top5)):  # Iterate through top 5 list
        dates, levels = fetch_measure_levels(top5[j][0].measure_id, dt=datetime.timedelta(days=dt))  # Find dates and
        # waterlevels for that station
        dateslist.append(dates)  # Add these dates to list
        levelslist.append(levels)  # Add the waterlevel data to list
        top5stations.append(top5[j][0])  # Add the stations to list
    return(plot_water_levels(top5stations, dateslist, levelslist))  # Use demonstrated function to display plot


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()


