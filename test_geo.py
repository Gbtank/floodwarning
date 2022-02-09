from floodsystem import geo
from floodsystem.stationdata import build_station_list

def test_stations_by_distance():
    stations = build_station_list()
    distance_stations = geo.stations_by_distance(stations, (52.2053, 0.1218))
    (first_station, distance) = distance_stations[0]
    # The closest station should be in Cambridge, provided it doesn't shut down.
    assert first_station.town == "Cambridge"

def test_stations_within_radius():
    stations = build_station_list()
    radius_stations = geo.stations_within_radius(stations, (52.2053, 0.1218), 10)
    name_list = [station.name for station in radius_stations]
    # This station is in Cambridge, so should be in the 10km radius, provided it doesn't shut down.
    assert "Cambridge Jesus Lock" in name_list

def test_rivers_with_station():
    stations = build_station_list()
    rivers = geo.rivers_with_station(stations)
    # Not precisely sure of the length as it changes, however, if it is less than 700,
    # something is likely to have gone wrong.
    assert len(rivers) > 700

def test_stations_by_river():
    stations = build_station_list()
    river_map = geo.stations_by_river(stations)
    test_stations = [station.name for station in river_map["River Cam"]]
    # Cam is a known station by the River Cam, so if it is not in the list, something went wrong.
    assert "Cam" in test_stations

def test_rivers_by_station_number():
    stations = build_station_list()
    # The length of the list must be 9 or greater, if it is not something went wrong.
    assert len(geo.rivers_by_station_number(stations, 9)) >= 9
