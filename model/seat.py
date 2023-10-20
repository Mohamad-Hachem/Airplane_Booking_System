class Seat:

    # initializing Seat class
    def __init__(self, seat_id: int, is_taken: bool = False, passenger_id: int = None):
        self.seat_id = seat_id
        self.is_taken = is_taken
        self.passenger_id = passenger_id

    def __str__(self):
        return (f"seat_id: {self.seat_id} "
                f"is_taken: {self.is_taken} "
                f"passenger_id: {self.passenger_id} ")
