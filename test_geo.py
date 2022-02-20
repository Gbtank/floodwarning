from unittest.mock import Mock
from floodsystem import geo
from floodsystem.stationdata import build_station_list

class MockStation():
    """This class represents a `mock` river level monitoring station
    used for testing the functionality of geo.py
    """

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

mockA = MockStation(0, 16, "A", (  0,   0), (0.0, 1.0), "Foo", "X")
mockB = MockStation(1, 17, "B", (0.5, 0.5), (0.2, 0.8), "Bar", "Y")
mockC = MockStation(2, 18, "C", (  5,   5), (0.4, 0.6), "Foo", "Z")
mockD = MockStation(3, 19, "D", ( 50,  50), (0.5, 0.5), "Baz", "X")
mockE = MockStation(4, 20, "E", ( 75,  75), (0.9, 0.1), "Baz", "Y")
mockF = MockStation(5, 21, "F", ( 99,  99),       None, "Bar", "Z")

stations = [mockA, mockC, mockB, mockE, mockD, mockF]

def test_stations_by_distance():
    distance_stations = geo.stations_by_distance(stations, (0, 0))
    (first_station, distance) = distance_stations[0]
    assert first_station == mockA

def test_stations_within_radius():
    radius_stations = geo.stations_within_radius(stations, (0, 0), 100)
    assert len(radius_stations) == 2
    assert radius_stations[0] == mockA

def test_rivers_with_station():
    rivers = geo.rivers_with_station(stations)
    assert len(rivers) == 3

def test_stations_by_river():
    river_map = geo.stations_by_river(stations)
    assert river_map == { "Foo": { mockA, mockC }, "Bar": { mockB, mockF }, "Baz": { mockD, mockE } }

def test_rivers_by_station_number():
    assert len(geo.rivers_by_station_number(stations, 1)) == 3
    assert len(geo.rivers_by_station_number(stations, 2)) == 3
    assert len(geo.rivers_by_station_number(stations, 3)) == 3
