from tests.fixture import reservations_instance


def test_initialization_and_str(reservations_instance):
    assert str(reservations_instance) == "This is the reservation_ids []"


def test_create_and_check_reservation(reservations_instance):
    reservations_instance.create_reservation(1, 101, 1001, 25)

    assert reservations_instance.does_reservation_exists(1) is True

    # Test creation of already existing reservation
    reservations_instance.create_reservation(1, 102, 1002, 26)
    # Reservation shouldn't be changed
    assert reservations_instance.reservation_list[1].airplane_id == 101
    assert reservations_instance.reservation_list[1].passenger_id == 1001
    assert reservations_instance.reservation_list[1].seat_number == 25


def test_cancel_reservation(reservations_instance, capsys):
    reservations_instance.create_reservation(1, 101, 1001, 25)
    reservations_instance.cancel_reservation(1)
    assert reservations_instance.does_reservation_exists(1) is False

    # Test cancellation of a non-existent reservation
    reservations_instance.cancel_reservation(2)
    captured = capsys.readouterr()
    assert captured.out == "There is no such reservation\n"


def test_modify_reservation(reservations_instance, capsys):
    reservations_instance.create_reservation(1, 101, 1001, 25)

    # Modify reservation
    reservations_instance.modify_reservation(1, 102, 1002, 26)
    assert reservations_instance.reservation_list[1].airplane_id == 102
    assert reservations_instance.reservation_list[1].passenger_id == 1002
    assert reservations_instance.reservation_list[1].seat_number == 26

    # Test modification of a non-existent reservation
    reservations_instance.modify_reservation(2, 103, 1003, 27)  # Assuming this reservation ID wasn't created.
    captured = capsys.readouterr()
    assert captured.out == "There is no such reservation\n"
