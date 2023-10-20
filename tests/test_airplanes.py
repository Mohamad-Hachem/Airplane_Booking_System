from tests.fixture import test_plane, test_airplanes, setup_airplanes_with_one_entry
from unittest.mock import patch
from model.small_plane import SmallPlane
from model.medium_plane import MediumPlane
from model.large_plane import LargePlane
from model.airplanes import Airplanes
from model.airplane import Airplane


def test_airplanes_initialization():
    airplanes = Airplanes()
    assert airplanes.airplanes_list == {}


def test_str_representation(test_airplanes: Airplanes):
    test_airplanes.airplanes_list = {1: 'plane1', 2: 'plane2'}
    assert str(test_airplanes) == "List of airplanes IDs: [1, 2]"


def test_create_small_plane_airplane(test_airplanes: Airplanes):
    # creating our needed inputs
    mock_inputs = ["S", 1, "AirFrance", "14:05:20", "16:20:30"]

    # generator that will give me the mock_inputs
    def mock_input_generator():
        for input_value in mock_inputs:
            yield input_value

    mock_input_side_effect = mock_input_generator()

    with patch('builtins.input', side_effect=mock_input_side_effect):
        test_airplanes.create_airplane()

    assert len(test_airplanes.airplanes_list) == 1
    assert type(test_airplanes.airplanes_list[1]) is SmallPlane


def test_create_medium_plane_airplane(test_airplanes: Airplanes):
    # Creating our needed inputs
    mock_inputs = ["M", 2, "Emirates", "15:00:00", "17:00:00"]

    # Generator that will yield the mock_inputs
    def mock_input_generator():
        for input_value in mock_inputs:
            yield input_value

    mock_input_side_effect = mock_input_generator()

    with patch('builtins.input', side_effect=mock_input_side_effect):
        test_airplanes.create_airplane()

    assert len(test_airplanes.airplanes_list) == 1
    assert type(test_airplanes.airplanes_list[2]) is MediumPlane


def test_create_large_plane_airplane(test_airplanes: Airplanes):
    # Creating our needed inputs
    mock_inputs = ["L", 3, "British Airways", "12:00:00", "18:00:00"]

    # Generator that will yield the mock_inputs
    def mock_input_generator():
        for input_value in mock_inputs:
            yield input_value

    mock_input_side_effect = mock_input_generator()

    with patch('builtins.input', side_effect=mock_input_side_effect):
        test_airplanes.create_airplane()

    assert len(test_airplanes.airplanes_list) == 1
    assert type(test_airplanes.airplanes_list[3]) is LargePlane


def test_does_airplane_exists_true(test_airplanes: Airplanes, test_plane: Airplane):
    test_airplanes.airplanes_list[test_plane.airplane_id] = test_plane

    assert test_airplanes.does_airplane_exists(1) is True


def test_does_airplane_exists_false(test_airplanes: Airplanes):

    assert test_airplanes.does_airplane_exists(1) is False


def test_modify_airplane_company_name(setup_airplanes_with_one_entry):
    mock_inputs = ["N", "AirCanada"]
    with patch('builtins.input', side_effect=mock_inputs):
        setup_airplanes_with_one_entry.modifying_airplane_information(1)
    assert setup_airplanes_with_one_entry.airplanes_list[1].company_name == "AirCanada"


def test_modify_airplane_departure_time(setup_airplanes_with_one_entry):
    mock_inputs = ["D", "15:00:00"]
    with patch('builtins.input', side_effect=mock_inputs):
        setup_airplanes_with_one_entry.modifying_airplane_information(1)
    assert setup_airplanes_with_one_entry.airplanes_list[1].departure_time == "15:00:00"


def test_modify_airplane_arrival_time(setup_airplanes_with_one_entry):
    mock_inputs = ["A", "17:00:00"]
    with patch('builtins.input', side_effect=mock_inputs):
        setup_airplanes_with_one_entry.modifying_airplane_information(1)
    assert setup_airplanes_with_one_entry.airplanes_list[1].arrival_time == "17:00:00"


def test_modify_airplane_invalid_command(setup_airplanes_with_one_entry, capsys):
    mock_inputs = ["Z"]
    with patch('builtins.input', side_effect=mock_inputs):
        setup_airplanes_with_one_entry.modifying_airplane_information(1)
    captured = capsys.readouterr()
    assert "You have entered an Invalid command please try again\n" in captured.out


def test_modify_non_existent_airplane(setup_airplanes_with_one_entry, capsys):
    setup_airplanes_with_one_entry.modifying_airplane_information(2)
    captured = capsys.readouterr()
    assert "This airplane does not exists create one or enter an airplane that exists" in captured.out


def test_delete_existing_airplane(setup_airplanes_with_one_entry, capsys):
    setup_airplanes_with_one_entry.delete_airplane(1)
    captured = capsys.readouterr()
    assert "the airplane with id: 1 is deleted successfully" in captured.out
    assert 1 not in setup_airplanes_with_one_entry.airplanes_list.keys()


def test_delete_non_existent_airplane(setup_airplanes_with_one_entry, capsys):
    setup_airplanes_with_one_entry.delete_airplane(3)
    captured = capsys.readouterr()
    assert "This airplane does not exists" in captured.out


def test_print_existing_airplane(setup_airplanes_with_one_entry, capsys):
    setup_airplanes_with_one_entry.print_airplane(1)
    captured = capsys.readouterr()
    assert str(setup_airplanes_with_one_entry.airplanes_list[1]) in captured.out


def test_print_non_existent_airplane(setup_airplanes_with_one_entry, capsys):
    setup_airplanes_with_one_entry.print_airplane(3)
    captured = capsys.readouterr()
    assert "This plane does not exists" in captured.out
