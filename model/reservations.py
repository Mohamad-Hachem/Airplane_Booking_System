from model.reservation import Reservation


class Reservations:

    # initializing class reservations
    def __init__(self):
        self.reservation_list = {}

    # printing the reservations
    def __str__(self):
        return f"This is the reservation_ids {[i for i in self.reservation_list.keys()]}"

    # does reservation exists
    def does_reservation_exists(self, reservation_id: int) -> bool:
        """
        This method allows you to check if reservation already exist
        :param reservation_id:
        :return: bool
        """
        return reservation_id in self.reservation_list.keys()

    # create a reservation
    def create_reservation(self, reservation_id: int, airplane_id: int, passenger_id: int, seat_number: int) -> None:
        """
        This method allows you to create reservation
        :param reservation_id:
        :param airplane_id:
        :param passenger_id:
        :param seat_number:
        :return: nothing(void)
        """
        if self.does_reservation_exists(reservation_id):
            print("reservation with this ID already exists")
        else:
            reservation = Reservation(reservation_id, airplane_id, passenger_id, seat_number)
            self.reservation_list[reservation_id] = reservation

    # cancel reservation
    def cancel_reservation(self, reservation_id: int) -> None:
        """
        this method allows you to cancel a reservation
        :param reservation_id:
        :return: nothing(void)
        """
        if self.does_reservation_exists(reservation_id):
            self.reservation_list.pop(reservation_id)
        else:
            print("There is no such reservation")

    # modify a reservation
    def modify_reservation(self, reservation_id: int, airplane_id: int, passenger_id: int, seat_number: int) -> None:
        """
        This method allows you to modify a reservation
        :param reservation_id:
        :param airplane_id:
        :param passenger_id:
        :param seat_number:
        :return: nothing(void)
        """
        if self.does_reservation_exists(reservation_id):
            self.reservation_list[reservation_id].airplane_id = airplane_id
            self.reservation_list[reservation_id].passenger_id = passenger_id
            self.reservation_list[reservation_id].seat_number = seat_number
        else:
            print("There is no such reservation")

    def print_reservation(self, reservation_id: int) -> None:
        """
        this method will allow you print a reservation
        :param reservation_id:
        :return: nothing(void)
        """
        if self.does_reservation_exists(reservation_id):
            print(self.reservation_list[reservation_id])
        else:
            print("this reservation doesn't exist")

    def all_passenger_reservations(self, passenger_id: int) -> None:
        """
        this method return all the reservation of a specific passenger
        :param passenger_id:
        :return: nothing(void)
        """
        for k, v in self.reservation_list.items():
            if v.passenger_id == passenger_id:
                self.print_reservation(k)
