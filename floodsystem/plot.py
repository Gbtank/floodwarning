# Plot submodule
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_water_levels(station, dates, levels):
    title = f"Station {station.name}"
    plt.plot(dates, levels)

    plt.xlabel("Date")
    plt.ylabel("Water Level (m)")
    plt.xticks(rotation=45)
    plt.title(title)

    plt.tight_layout()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    # TODO: Change title
    title = f"Station {station.name}"
    plt.plot(dates, levels)

    plt.xlabel("Date")
    plt.ylabel("Water Level (m)")
    plt.xticks(rotation=45)
    plt.title(title)

    # TODO: Also plot polynomial p

    plt.tight_layout()
    plt.show()
