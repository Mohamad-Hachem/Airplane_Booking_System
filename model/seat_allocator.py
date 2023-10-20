from model.seat import Seat


class SeatAllocator:

    # initializing SeatAllocator class
    def __init__(self, number_of_seats: int):
        self.list_of_seats = []
        for i in range(number_of_seats):
            self.list_of_seats.append(Seat(seat_id=i))

    # changing how printing SeatAllocator would look like
    def __str__(self):
        temp = "This is a map of the current available seats: \n"
        for i in self.list_of_seats:
            if i.is_taken:
                temp = temp + "| X |"
            else:
                temp = temp + f"| ✔({i.seat_id}) |"
        return temp

    # does seat exist
    def does_seat_exist(self, seat_id: int) -> bool:
        """
        this method allows you to check if a seat exists
        it takes
        :param seat_id:
        :return: nothing(void)
        """
        return 0 <= seat_id < len(self.list_of_seats)

    # checking if a seat is available
    def is_seat_available(self, seat_id: int) -> bool:
        """
        this method checks if a seat on an airplane is available
        :param seat_id:
        :return: boolean
        """
        if self.list_of_seats[seat_id].is_taken:
            return False
        return True

    # reserve a seat for a passenger
    def reserve_seat(self, passenger_id: int, seat_id: int) -> None:
        """
        The method will assign the seat to the passenger if it is available.
        it takes:
        :param passenger_id:
        :param seat_id:
        :return: nothing(void)
        """
        if self.does_seat_exist(seat_id):
            if self.is_seat_available(seat_id):
                # reserving the seat
                self.list_of_seats[seat_id].is_taken = True
                self.list_of_seats[seat_id].passenger_id = passenger_id
            else:
                print(f"This seat {seat_id} is already take please choose an other seat")
        else:
            print("Please enter a valid Seat")

    # releasing a seat
    def release_seat(self, seat_id: int) -> None:
        """
        This method makes a seat empty if it was already occupied.
        it takes:
        :param seat_id:
        :return: nothing(void)
        """
        if self.does_seat_exist(seat_id):
            if self.is_seat_available(seat_id):
                print(f"The seat {seat_id} is already empty")
            else:
                self.list_of_seats[seat_id].is_taken = False
                self.list_of_seats[seat_id].passenger_id = None
        else:
            print("Please enter a valid Seat")

    # change seat for a passenger
    def change_seat(self, passenger_id: int, seat_id_currently_taken: int, new_seat_id: int) -> None:
        """
        the method aims to change the seat of a passenger if possible. this method takes:
        :param passenger_id:
        :param seat_id_currently_taken:
        :param new_seat_id:
        :return: nothing(void)
        """
        if self.does_seat_exist(new_seat_id):
            if self.list_of_seats[seat_id_currently_taken].passenger_id == passenger_id:
                if self.is_seat_available(new_seat_id):
                    self.reserve_seat(passenger_id, new_seat_id)
                    self.release_seat(seat_id_currently_taken)
                else:
                    print(f"The seat {new_seat_id} you are trying to change to is not available")
            else:
                print(f"This seats {seat_id_currently_taken} does not belong to this passenger")
        else:
            print("Please enter a valid Seat")
