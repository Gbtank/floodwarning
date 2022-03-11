from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem import flood
import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.analysis import polyfit
    

def get_at_risk_towns(risk_thresholds,predictionAmount,N):
    """Print a list of towns that are predicted to have a increase in relative water level
    N - amount of towns considered
    predictionAmount - days into future predicted
    risk_thresholds - adjusts wording
    """
    #criteria: towns with stations that:
    # are in the top 60 highest relative level
    # and are predicted to have a rise in relative water level


        # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    # Setting the time interval to 2 days
    dt = 2

    # Run curve fitting with degree of 4
    p = 4

    shortlist = flood.stations_highest_rel_level(stations, N)
    
    # First find the stations at risk
    risk_stations = []

    for station in shortlist:
        dates, levels = fetch_measure_levels(station[0].measure_id,
                                             dt=datetime.timedelta(days=dt))
        if len(dates) < 1 or len(levels) < 1:
            # if there is no data, fitting will throw an error
            continue

        # calculate the fitting polynomial
        poly, d0 = polyfit(dates, levels, p)

        #get the list in date as float format
        x = plt.dates.date2num(dates)

        # get the latest date
        latestDate = max(x - d0)

        #amount of days to predict into the future
        predictionAmount = 2

        # predict the water level two days later
        prediction = poly(latestDate + predictionAmount)

        #get current relative water level
        r_level = station.relative_water_level()

        #get predicted water level
        predicted_r_level = predicted_relative_water_level(station, prediction)

        # calculate the predicted rise in relative water level
        rise = predicted_r_level - r_level

        #if relative level will rise add to at risk stations list
        if predicted_r_level > r_level:
            if station.town:
                risk_stations.append([station.town, rise])
            else:
                risk_stations.append(["Missing town name: at risk station is " +station.name, rise]) #fallback to station name if nearest town cannot be found
            

    at_risk_towns = []
    
    for i, station_i in enumerate(risk_stations): #loop through all stations at risk
        at_risk_towns.append(station_i[:]) # append town name and rise of station at risk

    # sort at_risk_towns by risks in descending order
    at_risk_towns.sort(key=lambda x: x[1], reverse=True)


    print("\nThe following warnings are for the top {} towns at risk, based on predictions for the next {} days".format(N,predictionAmount))
    print("Warnings will not be generated for towns already underwater\n")

    print("Current risk thresholds: \n ")
    
    ratings = ['low', 'moderate', 'high', 'severe']

    
    for i, threshold in enumerate(risk_thresholds):
        print("{} rating: {}".format(ratings[i+1],threshold))

    print('\nThe towns where the risk of flooding is assessed to be the greatest:')

    for town, relative_rise in at_risk_towns:
        rating_factor = 0  # low
        if relative_rise > risk_thresholds[0]:
            rating_factor = 1  # moderate
        if relative_rise > risk_thresholds[1]:
            rating_factor = 2  # high
        if relative_rise > risk_thresholds[2]:
            rating_factor = 3  # severe
        print('{}:\n\t{}'.format(town, ratings[rating_factor]))

def predicted_relative_water_level(station, prediction):
    """return predicted water level as fraction of the typical range"""

    #default case if data is not avaliable or inconsistent
    relative_level = None

    if station.typical_range_consistent():
        try:
            #should only work if data is consistent and avaliable
            relative_level = (prediction - station.typical_range[0]) / (
                station.typical_range[1] - station.typical_range[0])
        except:
            #if data is consistent but not present return None
            relative_level = None
        
    return relative_level    

def run():
    thresholds=[0.5,5,10]
    get_at_risk_towns(thresholds,2,60)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()