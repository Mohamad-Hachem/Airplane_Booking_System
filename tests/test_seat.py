import pytest
from model.seat import Seat


def test_seat_init_with_id_only():
    seat = Seat(1)
    assert seat.seat_id == 1
    assert seat.passenger_id is None
    assert seat.is_taken is False


def test_seat_init_with_id_and_is_taken():
    seat = Seat(1, True)
    assert seat.seat_id == 1
    assert seat.passenger_id is None
    assert seat.is_taken is True


def test_seat_init_with_all_attributes():
    seat = Seat(1, False, 4)
    assert seat.seat_id == 1
    assert seat.passenger_id == 4
    assert seat.is_taken is False


def test_str_representation():
    # Arrange
    seat_id = 1
    is_taken = False
    passenger_id = None
    seat = Seat(seat_id, is_taken, passenger_id)
    expected_str = (f"seat_id: {seat_id} "
                    f"is_taken: {is_taken} "
                    f"passenger_id: {passenger_id} ")

    # Act
    result_str = str(seat)

    # Assert
    assert result_str == expected_str
