from model.reservation import Reservation


def test_reservation_initialization():
    # Creating a reservation instance
    reservation = Reservation(1, 101, 1001, 25)

    # Assertions to check if all attributes are correctly initialized
    assert reservation.reservation_id == 1
    assert reservation.airplane_id == 101
    assert reservation.passenger_id == 1001
    assert reservation.seat_number == 25


def test_reservation_string_representation():
    # Creating a reservation instance
    reservation = Reservation(1, 101, 1001, 25)

    # Expected string representation
    expected_str = ("-------------------------------\n"
                    "Reservation Information:\n"
                    "reservation_id: 1\n"
                    "airplane_id: 101\n"
                    "passenger_id : 1001\n"
                    "seat_number: 25\n"
                    "-------------------------------\n")

    # Assertion to check if the string representation is correct
    assert str(reservation) == expected_str
