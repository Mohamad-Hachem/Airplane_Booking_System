class Reservation:

    # initializing the reservation class
    def __init__(self, reservation_id: int, airplane_id: int, passenger_id: int, seat_number: int):
        self.reservation_id = reservation_id
        self.airplane_id = airplane_id
        self.passenger_id = passenger_id
        self.seat_number = seat_number

    # print reservation
    def __str__(self):
        return (f"-------------------------------\n"
                f"Reservation Information:\n"
                f"reservation_id: {self.reservation_id}\n"
                f"airplane_id: {self.airplane_id}\n"
                f"passenger_id : {self.passenger_id}\n"
                f"seat_number: {self.seat_number}\n"
                f"-------------------------------\n")
