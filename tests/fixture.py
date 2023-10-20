import pytest
from datetime import time
from model.airplane import Airplane
from model.airplanes import Airplanes
from model.passenger import Passenger
from model.passengers import Passengers
from model.small_plane import SmallPlane
from model.reservations import Reservations


@pytest.fixture
def test_plane():
    airplane_id = 1
    company_name = "AirFrance"
    departure_time = time(14, 20, 10)
    arrival_time = time(16, 20, 10)
    return Airplane(airplane_id, company_name, departure_time, arrival_time)


@pytest.fixture
def test_airplanes():
    return Airplanes()


@pytest.fixture
def test_passenger():
    return Passenger(1, "mohamad", "hachem")


@pytest.fixture
def test_passengers():
    return Passengers()


@pytest.fixture
def setup_airplanes_with_one_entry():
    airplanes = Airplanes()
    airplane = SmallPlane(1, "AirFrance",
                          "14:05:20", "16:20:30")
    airplanes.airplanes_list[1] = airplane
    return airplanes


@pytest.fixture
def reservations_instance():
    return Reservations()
