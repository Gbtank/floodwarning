from floodsystem.stationdata import build_station_list
from floodsystem import geo

def run():
    stations = build_station_list()

    rivers = geo.rivers_by_station_number(stations, 9)
    print(rivers)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***") 
    run()
