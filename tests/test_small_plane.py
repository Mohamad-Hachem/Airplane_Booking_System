from datetime import time
from model.small_plane import SmallPlane
from model.seat_allocator import SeatAllocator


def test_small_plane_initialization():
    airplane_id = 1
    company_name = "AirFrance"
    departure = time(14, 20, 10)
    arrival = time(16, 20, 10)

    plane = SmallPlane(airplane_id, company_name, departure, arrival)

    assert plane.airplane_id == airplane_id
    assert plane.company_name == company_name
    assert plane.departure_time == departure
    assert plane.arrival_time == arrival
    assert isinstance(plane.seat_allocator, SeatAllocator)
    assert len(plane.seat_allocator.list_of_seats) == 4


def test_small_plane_str_representation():
    airplane_id = 1
    company_name = "AirFrance"
    departure = time(14, 20, 10)
    arrival = time(16, 20, 10)

    plane = SmallPlane(airplane_id, company_name, departure, arrival)

    expected_str = (f"---------------------------\n"
                    f"Airplane details:\nID: {airplane_id}\nCompany Name: {company_name}\nDeparture Time: "
                    f"{departure} \nArrival Time: {arrival}\n"
                    f"---------------------------\n"
                    f"{str(plane.seat_allocator)}\n---------------------------\n")

    assert str(plane) == expected_str
