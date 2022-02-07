from floodsystem import geo
from floodsystem.stationdata import build_station_list

class TestStation:
    def __init__(self, name, river):
        self.name = name
        self.river = river

def test_rivers_with_station():
    stationOne = TestStation("One", "A")
    stationTwo = TestStation("Two", "B")
    stationThree = TestStation("Three", "A")

    stations = [ stationOne, stationTwo, stationThree ]
    river_map = geo.stations_by_river(stations)
    print(river_map)

def test_rivers_by_station_number():
    stations = build_station_list()
    river_list = geo.rivers_by_station_number(stations, 6)
    print(river_list)
    river_list = geo.rivers_by_station_number(stations, 7)
    print(river_list)
    river_list = geo.rivers_by_station_number(stations, 8)
    print(river_list)

