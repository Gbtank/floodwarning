import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.utils import sorted_by_key
import datetime

# p=10
# dt=10
# stations = build_station_list()

# dates, levels = fetch_measure_levels(stations[153].measure_id, dt=datetime.timedelta(days=dt))
# poly, d0 = polyfit(dates, levels, p)
# datesnum = matplotlib.dates.date2num(dates)
# plt.plot(dates, levels, color="r")
# plt.plot(dates, poly(datesnum-d0))
# plt.show()


def run():
    """Demonstration function for task 2F
    """
    stations = build_station_list()  # Create list of all stations
    update_water_levels(stations)  # Update the water levels

    dt = 2  # Number of days to plot
    N = 5  # Number of stations to plot
    p = 4  # Degree of polynomial to use for the bestfit plot

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
    for j in range(len(top5)):  # Iterate through top 5 list
        dates, levels = fetch_measure_levels(top5[j][0].measure_id, dt=datetime.timedelta(days=dt))  # Find dates and
        # waterlevels for that station
        plt.figure(j)  # Create a new plot for this station
        plot_water_level_with_fit(top5[j][0], dates, levels, p)  # Use the function created in task 2F
        # to plot the graph
    plt.show()  # Show the plot


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()