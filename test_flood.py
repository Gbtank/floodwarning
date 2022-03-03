import pytest
from floodsystem import flood

class MockStation():
    """This class represents a `mock` river level monitoring station
    used for testing the functionality of geo.py
    """

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town, latest_level):

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

        self.latest_level = latest_level

    
    def typical_range_consistent(self):
        if self.typical_range is None:
            return False
        (low, high) = self.typical_range
        return low < high

    def relative_water_level(self):
        if not self.typical_range_consistent() or self.latest_level is None:
            return None

        (low, high) = self.typical_range
        
        # Normalise range and water level with respect to low.
        # e.g. if rel = 5, high = 3, low = 1
        # equivalently, rel = 4, high = 2, low = 0
        # now its obvious rel is 2.0 of the fraction
        real_range = high - low
        norm_water = self.latest_level - low
        return norm_water / real_range

mockA = MockStation(0, 16, "A", (  0,   0), (0.0, 1.0), "Foo", "X", 0.5)
mockB = MockStation(1, 17, "B", (0.5, 0.5), (0.2, 1.0), "Bar", "Y", 0.4)
mockC = MockStation(2, 18, "C", (  5,   5), (0.4, 0.6), "Foo", "Z", 0.2)
mockD = MockStation(3, 19, "D", ( 50,  50), (0.5, 0.5), "Baz", "X", None)
mockE = MockStation(4, 20, "E", ( 75,  75), (0.9, 0.1), "Baz", "Y", 0.7)
mockF = MockStation(5, 21, "F", ( 99,  99),       None, "Bar", "Z", 0.8)

stations = [mockA, mockC, mockB, mockE, mockD, mockF]

def test_stations_level_over_threshold():
    result = flood.stations_level_over_threshold(stations, 0.0)
    assert result == [(mockA, 0.5), (mockB, 0.25)]

def test_stations_highest_rel_level():
    result = flood.stations_highest_rel_level(stations, 2)
    assert result[0] == (mockA, 0.5)
    assert result[1] == (mockB, 0.25)