from unittest.mock import patch

from tests.fixture import test_passenger, test_passengers
from model.passenger import Passenger
from model.passengers import Passengers


def test_initialization():
    p = Passengers()
    assert p.passengers_list == {}


def test_str_representation(test_passenger: Passenger, test_passengers: Passengers):
    passenger = test_passenger
    passenger_id = passenger.passenger_id
    test_passengers.passengers_list[passenger_id] = passenger

    expected_str = f"List of passenger ID [{passenger_id}]"
    assert str(test_passengers) == expected_str


def test_does_passenger_exist(test_passenger: Passenger, test_passengers: Passengers):
    passenger_id = test_passenger.passenger_id
    test_passengers.passengers_list[passenger_id] = test_passenger

    assert test_passengers.does_passenger_exist(passenger_id) is True
    assert test_passengers.does_passenger_exist(-999) is False


def test_adding_passenger(test_passenger: Passenger, test_passengers: Passengers):
    # Extract passenger details from the test_passenger fixture
    passenger_id = test_passenger.passenger_id
    first_name = test_passenger.first_name
    last_name = test_passenger.last_name

    # Add passenger using the adding_passenger method
    test_passengers.add_passenger(passenger_id, first_name, last_name)

    # Check if the passenger was added
    assert test_passengers.does_passenger_exist(passenger_id) is True


def test_adding_existing_passenger(test_passenger: Passenger, test_passengers: Passengers, capsys):
    # Extract passenger details from the test_passenger fixture
    passenger_id = test_passenger.passenger_id
    first_name = test_passenger.first_name
    last_name = test_passenger.last_name

    # First, add passenger using the adding_passenger method
    test_passengers.add_passenger(passenger_id, first_name, last_name)

    # Attempt to add the same passenger again
    test_passengers.add_passenger(passenger_id, first_name, last_name)

    # Capture stdout using pytest's capsys
    captured = capsys.readouterr()

    # Verify that the print statement outputs the expected message
    assert captured.out == "a passenger with this id already exists\n"


def test_modify_existing_passenger_first_name(test_passenger: Passenger, test_passengers: Passengers, monkeypatch):
    passenger_id = test_passenger.passenger_id
    test_passengers.passengers_list[passenger_id] = test_passenger
    # creating our needed inputs
    mock_inputs = ["F", "NewFirstName"]

    # generator that will give me the mock_inputs
    def mock_input_generator():
        for input_value in mock_inputs:
            yield input_value

    mock_input_side_effect = mock_input_generator()

    with patch('builtins.input', side_effect=mock_input_side_effect):
        test_passengers.modify_passenger(passenger_id)

    assert test_passengers.passengers_list[passenger_id].first_name == "NewFirstName"


def test_modify_existing_passenger_last_name(test_passenger: Passenger, test_passengers: Passengers):
    passenger_id = test_passenger.passenger_id
    test_passengers.passengers_list[passenger_id] = test_passenger
    # creating our needed inputs
    mock_inputs = ["L", "NewLastName"]

    # generator that will give me the mock_inputs
    def mock_input_generator():
        for input_value in mock_inputs:
            yield input_value

    mock_input_side_effect = mock_input_generator()

    with patch('builtins.input', side_effect=mock_input_side_effect):
        test_passengers.modify_passenger(passenger_id)

    assert test_passengers.passengers_list[passenger_id].last_name == "NewLastName"


def test_modify_non_existing_passenger(test_passengers: Passengers, capsys):
    passenger_id = -999  # An ID that doesn't exist

    with patch('builtins.input', return_value="F"):
        test_passengers.modify_passenger(passenger_id)

    captured = capsys.readouterr()
    assert captured.out == "This passenger does not exist, create one first\n"


def test_delete_existing_passenger(test_passenger: Passenger, test_passengers: Passengers, capsys):
    passenger_id = test_passenger.passenger_id
    test_passengers.passengers_list[passenger_id] = test_passenger

    test_passengers.delete_passenger(passenger_id)
    captured = capsys.readouterr()
    assert f"the passenger with id {passenger_id} is deleted" in captured.out
    assert passenger_id not in test_passengers.passengers_list


def test_delete_non_existing_passenger(test_passengers: Passengers, capsys):
    passenger_id = -999  # An ID that doesn't exist

    test_passengers.delete_passenger(passenger_id)
    captured = capsys.readouterr()
    assert "This passenger does not exist" in captured.out


def test_print_existing_passenger_info(test_passenger: Passenger, test_passengers: Passengers, capsys):
    passenger_id = test_passenger.passenger_id
    test_passengers.passengers_list[passenger_id] = test_passenger

    test_passengers.print_passenger_info(passenger_id)
    captured = capsys.readouterr()
    expected_output = (f"Passenger_ID: {passenger_id}\nFirst_name: {test_passenger.first_name}\nLast_name: "
                       f"{test_passenger.last_name}")
    assert expected_output in captured.out


def test_print_non_existing_passenger_info(test_passengers: Passengers, capsys):
    passenger_id = -999  # An ID that doesn't exist

    test_passengers.print_passenger_info(passenger_id)
    captured = capsys.readouterr()
    assert "This passenger does not exist" in captured.out
