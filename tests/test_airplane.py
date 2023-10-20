from tests.fixture import test_plane
from datetime import time
from model.airplane import Airplane


def test_airplane_initialization(test_plane):
    airplane = test_plane

    assert airplane.airplane_id == test_plane.airplane_id
    assert airplane.company_name == test_plane.company_name
    assert airplane.departure_time == test_plane.departure_time
    assert airplane.arrival_time == test_plane.arrival_time


def test_airplane_str_representation(test_plane):
    airplane = test_plane

    expected_str = (f"---------------------------\n"
                    f"Airplane details:\nID: {test_plane.airplane_id}\nCompany Name: {test_plane.company_name}\nDeparture Time: "
                    f"{test_plane.departure_time} \nArrival Time: {test_plane.arrival_time}\n"
                    f"---------------------------\n")

    assert str(airplane) == expected_str


def test_change_airplane_name(test_plane):
    airplane = test_plane

    # Change company name and test
    new_company_name = "Delta"
    airplane.change_airplane_name(new_company_name)
    assert airplane.company_name == new_company_name


def test_change_departure_time(test_plane):
    airplane = test_plane

    # Change departure time and test
    new_departure_time = time(15, 30, 45)
    airplane.change_departure_time(new_departure_time)
    assert airplane.departure_time == new_departure_time


def test_change_arrival_time(test_plane):
    airplane = test_plane

    # Change arrival time and test
    new_arrival_time = time(17, 45, 55)
    airplane.change_arrival_time(new_arrival_time)
    assert airplane.arrival_time == new_arrival_time
