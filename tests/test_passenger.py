from model.passenger import Passenger
from tests.fixture import test_passenger


def test_passenger_initialization(test_passenger: Passenger):
    passenger = test_passenger

    assert passenger.passenger_id == 1
    assert passenger.first_name == "mohamad"
    assert passenger.last_name == "hachem"


def test_passenger_str_representation(test_passenger: Passenger):
    passenger = test_passenger
    expected_str = ("---------------------------------\n"
                    "Passenger information\n"
                    "Passenger_ID: 1\nFirst_name: mohamad\nLast_name: hachem\n"
                    "---------------------------------\n")

    assert str(passenger) == expected_str


def test_modifying_first_name(test_passenger: Passenger):
    passenger = test_passenger
    passenger.modifying_first_name("john")

    assert passenger.first_name == "john"


def test_modifying_last_name(test_passenger: Passenger):
    passenger = test_passenger
    passenger.modifying_last_name("doe")

    assert passenger.last_name == "doe"
