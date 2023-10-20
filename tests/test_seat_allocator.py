from model.seat_allocator import SeatAllocator
from model.seat import Seat


def test_init_seat_allocator():
    list_result = SeatAllocator(3).list_of_seats
    # Assert
    assert len(list_result) == 3
    assert type(list_result[0]) == Seat
    assert list_result[0].seat_id == 0
    assert isinstance(list_result[0], Seat)


def test_str_seat_allocator():
    # act
    seat_allocator = SeatAllocator(3)
    expected_str = "This is a map of the current available seats: \n| ✔(0) || ✔(1) || ✔(2) |"

    # Arrange
    result_str = str(seat_allocator)

    # Assert
    assert result_str == expected_str


def test_is_seat_available_when_available():
    seat_allocator = SeatAllocator(3)

    result = seat_allocator.is_seat_available(1)

    assert result is True


def test_is_seat_available_when_not_available():
    seat_allocator = SeatAllocator(3)
    seat_allocator.reserve_seat(1, 1)

    result = seat_allocator.is_seat_available(1)

    assert result is False


def test_reserve_seat_when_available():
    seat_allocator = SeatAllocator(3)
    seat_allocator.reserve_seat(1, 1)

    result_seat_is_taken = seat_allocator.list_of_seats[1].is_taken
    result_seat_passenger_id = seat_allocator.list_of_seats[1].passenger_id

    assert result_seat_is_taken is True
    assert result_seat_passenger_id == 1


def test_reserve_seat_when_not_available(capsys):
    seat_allocator = SeatAllocator(3)
    seat_allocator.reserve_seat(1, 1)

    # reserving already existing one
    seat_allocator.reserve_seat(1, 1)

    captured = capsys.readouterr()  # capture print outputs
    assert captured.out == "This seat 1 is already take please choose an other seat\n"


def test_release_seat_when_taken():
    seat_allocator = SeatAllocator(3)
    seat_allocator.reserve_seat(1, 1)

    seat_allocator.release_seat(1)

    assert seat_allocator.list_of_seats[1].is_taken is False
    assert seat_allocator.list_of_seats[1].passenger_id is None


def test_release_seat_when_not_taken(capsys):
    seat_allocator = SeatAllocator(3)

    # reserving already existing one
    seat_allocator.release_seat(1)

    captured = capsys.readouterr()  # capture print outputs
    assert captured.out == "The seat 1 is already empty\n"


def test_change_seat_when_seat_is_for_passenger_and_seat_available():
    seat_allocator = SeatAllocator(3)
    seat_allocator.reserve_seat(1, 1)

    seat_allocator.change_seat(1, 1, 2)

    assert seat_allocator.list_of_seats[1].is_taken is False
    assert seat_allocator.list_of_seats[1].passenger_id is None
    assert seat_allocator.list_of_seats[2].is_taken is True
    assert seat_allocator.list_of_seats[2].passenger_id is 1


def test_change_seat_when_seat_is_for_passenger_and_seat_not_available(capsys):
    seat_allocator = SeatAllocator(3)
    seat_allocator.reserve_seat(1, 1)
    seat_allocator.reserve_seat(2, 2)

    seat_allocator.change_seat(1, 1, 2)

    captured = capsys.readouterr()  # capture print outputs
    assert captured.out == "The seat 2 you are trying to change to is not available\n"


def test_change_seat_when_seat_not_for_passenger_and_seat_available(capsys):
    seat_allocator = SeatAllocator(3)
    seat_allocator.reserve_seat(1, 1)
    seat_allocator.reserve_seat(2, 2)

    seat_allocator.change_seat(1, 2, 2)

    captured = capsys.readouterr()  # capture print outputs
    assert captured.out == "This seats 2 does not belong to this passenger\n"
