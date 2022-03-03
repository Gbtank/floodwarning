from floodsystem.station import MonitoringStation
import matplotlib.pyplot as plt
import matplotlib
from floodsystem.analysis import polyfit


def plot_water_levels(station, dates, levels):  # Task 2E new function
    """Displays a plot of the water level data against time, with
    typical high/low levels for comparison.
    Inputs are "station" (one station or a list of stations
    (of type MonitoringStation)), "dates" (a list of dates in the form
    YYYY-MM-DD), and "levels" (one or a list of floats corresponding to
    each station)
    """
    if type(station) is MonitoringStation:  # Check if it is one station
        # Set the typical High and Low waterlevel values
        typicalhigh = station.typical_range[1]
        typicallow = station.typical_range[0]

        plt.plot(dates, levels, label="Waterlevel data")  # Use matplotlib to plot the dates against waterlevels
        plt.axhline(typicalhigh, color="b", linestyle="dashed", label="Typical High Waterlevel")  # Add
        # line for typical high level
        plt.axhline(typicallow, color="r", linestyle="dashed", label="Typical Low Waterlevel")  # Add
        # line for typical low level
        plt.xlabel("Date")  # Label x axis
        plt.xticks(rotation=45)  # rotate date labels so that they fit better
        plt.ylabel("Water Level (m)")  # Label y axis
        plt.title(station.name)  # Add the station name as the title of the plot
        plt.tight_layout  # ensure plot doesn't cut off date labels
        plt.legend(loc="best")  # Move the legend to the place on the graph where it overlaps the least data

    elif type(station) is list:  # Check if it is a list of stations
        if len(station) > 1:  # Make sure there is more than one station in the list
            fig, axs = plt.subplots(len(station), sharex=True)  # Create a figure for the subplots (with a
            # shared x (dates) axis)
            fig.suptitle("Water Level Data for Stations with Top " + str(len(station)) + (
                " (relative) Water Levels (Best Viewed Fullscreen)"))  # Overall plot title
            for i in range(len(station)):  # Iterate through list of stations to create subplots
                axs[i].plot(dates[i], levels[i], label=("Waterlevel data for " + station[i].name))  # Create
                # subplot with a label for the waterlevel data
                # Set the typical High and Low waterlevel values
                typicalhigh = station[i].typical_range[1]
                typicallow = station[i].typical_range[0]

                axs[i].axhline(typicalhigh, color="b", linestyle="dashed", label=(
                    "Typical High Waterlevel for " + station[i].name))  # Add line for typical high level
                axs[i].axhline(typicallow, color="r", linestyle="dashed", label=(
                    "Typical Low Waterlevel for " + station[i].name))  # Add line for typical low level
                axs[i].set(ylabel="Water Level (m)")  # Label axes
                axs[i].set_title(station[i].name)  # Add the station name as the title of the subplot
                axs[i].legend(loc="best")  # Move the legend to the place on the subplot where it overlaps
                # the least data
            axs[-1].set(xlabel="Date")  # Add the x-axis label to the singular x-axis (on the bottom)
        elif len(station) == 1:  # If the list is of just 1 station, then it cannot iterate through and
            # needs another way to plot it
            typicalhigh = station[0].typical_range[1]
            typicallow = station[0].typical_range[0]

            plt.plot(dates[0], levels[0], label="Waterlevel data")  # Use matplotlib to plot the dates
            # against waterlevels

            # Add line for typical high level
            plt.axhline(typicalhigh, color="b", linestyle="dashed", label="Typical High Waterlevel")

            # Add line for typical low level
            plt.axhline(typicallow, color="r", linestyle="dashed", label="Typical Low Waterlevel")

            plt.xlabel("Date")  # Label x axis
            plt.xticks(rotation=45)  # rotate date labels so that they fit better
            plt.ylabel("Water Level (m)")  # Label y axis
            plt.title(station[0].name)  # Add the station name as the title of the plot
            plt.tight_layout  # ensure plot doesn't cut off date labels
            plt.legend(loc="best")  # Move the legend to the place on the graph where it overlaps the least data
    else:  # Raise an error if the input is not of the correct type
        raise TypeError(" 'Station' must be of type MonitoringStation, or a list of MonitoringStation objects")

    plt.show()  # Display plot


def plot_water_level_with_fit(station, dates, levels, p):
    """Function to plot water level (list of floats) data of a station (of type
    MonitoringStation) for a list of dates (YYYY-MM-DD) alongside
    the best-fit polynomial of order "p (float)"
    """
    try:  # Make sure the date list is of the correct type
        assert type(dates) == list
    except AssertionError:  # Print error message
        print("""Type of dates is incorrect. They should be a list of dates
        in form YYYY-MM-DD""")
    try:  # Make sure the levels list is of the correct type
        assert type(levels) == list
    except AssertionError:  # Print error message
        print("""Type of levels is incorrect. They should be a list of floats""")
    try:  # Make sure the polynomial degree (p) is of the correct type
        assert type(p) == int
    except AssertionError:  # Print error message
        print("""Type of p is incorrect. They should be a integer""")

    datesnum = matplotlib.dates.date2num(dates)  # Convert dates in form YYYY-MM-DD to
    # numerical form
    poly, d0 = polyfit(dates, levels, p)  # Use polyfit function to find the best-fit polynomial
    plt.plot(dates, poly(datesnum - d0), color="m", label="Best-fit polynomial")  # Plot best-fit polynomial

    if type(station) is MonitoringStation:  # Make sure station is of the right type
        # Set the typical High and Low waterlevel values
        typicalhigh = station.typical_range[1]
        typicallow = station.typical_range[0]

        plt.plot(dates, levels, color="g", label="Waterlevel data")  # Use matplotlib to plot the dates against
        # waterlevels
        plt.axhline(typicalhigh, color="b", linestyle="dashed", label="Typical High Waterlevel")  # Add
        # line for typical high level
        plt.axhline(typicallow, color="r", linestyle="dashed", label="Typical Low Waterlevel")  # Add
        # line for typical low level
        plt.xlabel("Date")  # Label x axis
        plt.xticks(rotation=45)  # rotate date labels so that they fit better
        plt.ylabel("Water Level (m)")  # Label y axis
        plt.title(station.name)  # Add the station name as the title of the plot
        plt.tight_layout  # ensure plot doesn't cut off date labels
        plt.legend(loc="best")  # Move the legend to the place on the graph where it overlaps the least data
    else:
        raise TypeError("Station must be of type MonitoringStation")  # Raise an exception

    plt.tight_layout()  # Fix the layout of the graph

    # plt.show()  # Display plot (must be used at end, so commented out in order to
    # allow this function to be used multiple times to make more than one plot)